# Source rules

- Keep modules focused by domain responsibility.
- Connector modules only fetch/map provider responses; they do not write SQLite.
- `service.py` owns orchestration and job progression.
- `canonical.py` contains pure identity rules.
- `storage.py`, `jobs.py`, `artifacts.py`, and `export.py` contain explicit side effects.
- Do not add provider-specific fields to canonical storage without a schema/design review.
