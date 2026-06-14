#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLUGIN = ROOT / "plugins" / "avengers"

AGENTS = {
    "captain-america",
    "iron-man",
    "spider-man",
    "doctor-strange",
    "black-widow",
    "hawkeye",
    "hulk",
    "ant-man",
    "black-panther",
    "nick-fury",
    "jarvis",
}

COMMANDS = {
    "audit",
    "brainstorm",
    "plan",
    "feature",
    "bugfix",
    "fix",
    "debug",
    "explain",
    "pr",
    "refactor",
    "report",
    "research",
    "review",
    "test",
    "commit",
    "init",
}
SKILLS = {
    "audit-first",
    "auto-init",
    "build-patterns",
    "captain-america",
    "core-principles",
    "git-safety",
    "hulk",
    "memory",
    "nick-fury",
    "scoped-fix",
    "test-strategies",
    "verification",
}
KNOWLEDGE = {
    "build-patterns.md",
    "core-principles.md",
    "workflow-rules.md",
    "review-checklist.md",
    "security-checklist.md",
    "testing-checklist.md",
    "test-strategies.md",
    "git-rules.md",
    "memory-system.md",
}


def fail(message: str) -> None:
    print(f"FAIL: {message}")
    sys.exit(1)


def read_json(path: Path) -> dict:
    try:
        return json.loads(path.read_text())
    except Exception as exc:
        fail(f"{path} is not valid JSON: {exc}")


def frontmatter(path: Path) -> dict[str, object]:
    text = path.read_text()
    match = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not match:
        fail(f"{path} is missing YAML frontmatter")
    data: dict[str, object] = {}
    current: str | None = None
    for raw in match.group(1).splitlines():
        if re.match(r"^[A-Za-z0-9_-]+:", raw):
            key, value = raw.split(":", 1)
            current = key.strip()
            data[current] = value.strip()
        elif raw.startswith("  - ") and current:
            data.setdefault(current, [])
            if not isinstance(data[current], list):
                data[current] = []
            data[current].append(raw[4:].strip())
    return data


def main() -> None:
    read_json(ROOT / ".codex-plugin" / "plugin.json")
    marketplace = read_json(ROOT / ".claude-plugin" / "marketplace.json")
    plugin_json = read_json(PLUGIN / ".claude-plugin" / "plugin.json")

    if marketplace["plugins"][0]["version"] != plugin_json["version"]:
        fail("Claude marketplace and plugin versions differ")

    for agent in AGENTS:
        path = PLUGIN / "agents" / f"{agent}.md"
        if not path.exists():
            fail(f"missing agent {agent}")
        fm = frontmatter(path)
        if fm.get("name") != agent:
            fail(f"agent name mismatch in {path}")
        for skill in fm.get("skills", []):
            if skill not in SKILLS:
                fail(f"{path} references missing skill {skill}")

    for command in COMMANDS:
        path = PLUGIN / "commands" / f"{command}.md"
        if not path.exists():
            fail(f"missing command {command}")
        fm = frontmatter(path)
        if "description" not in fm or "allowed-tools" not in fm:
            fail(f"command metadata incomplete in {path}")

    for skill in SKILLS:
        path = PLUGIN / "skills" / skill / "SKILL.md"
        if not path.exists():
            fail(f"missing skill {skill}")
        fm = frontmatter(path)
        if fm.get("name") != skill:
            fail(f"skill name mismatch in {path}")

    for knowledge in KNOWLEDGE:
        if not (PLUGIN / "knowledge" / knowledge).exists():
            fail(f"missing knowledge file {knowledge}")

    hooks = PLUGIN / "hooks" / "hooks.json"
    session_start = PLUGIN / "hooks" / "session-start.sh"
    if not hooks.exists():
        fail("missing hooks/hooks.json")
    read_json(hooks)
    if not session_start.exists():
        fail("missing hooks/session-start.sh")
    if not (session_start.stat().st_mode & 0o111):
        fail("hooks/session-start.sh is not executable")

    forbidden_parts = [
        ("Shankar", "Kakumani"),
        ("shankar", "@"),
        ("transformers", "@", "transformers"),
        (".claude", "transformers"),
    ]
    for path in ROOT.rglob("*"):
        if path == Path(__file__).resolve():
            continue
        if path.is_file() and ".git" not in path.parts:
            try:
                text = path.read_text()
            except UnicodeDecodeError:
                continue
            for parts in forbidden_parts:
                token = "".join(parts)
                if token in text:
                    fail(f"forbidden upstream token {token!r} in {path}")

    print("OK: Avengers Agents structure is valid")


if __name__ == "__main__":
    main()
