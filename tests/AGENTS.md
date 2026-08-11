# Test rules

- Write the failing test before production behavior.
- Pure-function tests use real inputs and no mocks.
- HTTP tests use deterministic `httpx.MockTransport`; do not require live network.
- SQLite tests use pytest temporary directories.
- Test output files go under pytest temp directories or `tests/output/`.
