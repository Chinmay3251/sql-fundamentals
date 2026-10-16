# Manual verification checklist

- [ ] Confirm `DATABASE_URL` uses a least-privilege read-only account.
- [ ] Confirm Vanna model/provider and version match the approved environment.
- [ ] Load the actual schema and train the five examples from `TRAINING_PAIRS`.
- [ ] Run all ten questions in `test_queries.md`.
- [ ] Inspect each SQL statement before execution.
- [ ] Execute only approved read-only queries against a safe test database.
- [ ] Compare results with a trusted query or known sample.
- [ ] Check invalid input and provider failure behavior.
- [ ] Confirm execution remains disabled in this starter.
- [ ] Record actual outcomes; do not mark checks complete unless performed.

## Current status

The repository includes automated unit tests for API behavior when the provider is unconfigured and for basic SQL safety. Live Vanna generation and database connectivity have **not** been verified because credentials, the actual schema, and approved provider configuration were not supplied.
