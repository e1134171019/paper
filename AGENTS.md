# Collector Core project rules

- Follow the user-owned Python project standard from the AI Work System.
- Python 3.11+.
- All Python files are UTF-8 and start with `# -*- coding: utf-8 -*-`.
- All function parameters and return values are typed.
- Domain records use frozen dataclasses; lifecycle states use Enum.
- Keep canonicalization and identity rules pure.
- Keep HTTP, SQLite, filesystem, and CSV operations at explicit side-effect boundaries.
- SQLite is the source of truth; CSV is derived.
- Do not bypass paywalls, CAPTCHAs, access controls, or publisher credentials.
- Do not commit downloaded publisher PDFs to this public repository.
- New behavior follows test-first RED -> GREEN -> refactor.
