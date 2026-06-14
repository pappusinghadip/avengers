# Testing Checklist

Use this for Hulk and verification tasks.

- Find the repo-native test command before inventing one.
- If no test framework exists, use targeted smoke checks and static review.
- Cover happy path, empty/null, boundary values, failed dependency, and permission failure.
- For frontend, check loading, empty, error, and mobile/responsive states.
- For backend, check API contract, status/body, persistence, cache invalidation, and logs.
- Report exact commands run and whether they passed.
