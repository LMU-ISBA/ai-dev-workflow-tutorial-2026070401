# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Two things at once:

- A **tutorial** that teaches an AI-assisted development workflow. The prose lives in `README.md`, `pre-work-setup.md`, and `workshop-build-deploy.md`, and is written for students.
- The **dashboard those docs have you build**: a Streamlit e-commerce sales dashboard (`app.py`, `data.py`, `tests/`), built from the spec in `prd/ecommerce-analytics.md`.

When you change the app, check whether the tutorial prose still describes it accurately, and vice versa. The docs walk a student through producing this exact app, so the two need to stay in sync.

## Commands

All Python work runs inside the `venv/` virtual environment:

```bash
source venv/bin/activate                            # activate first
streamlit run app.py                                # run the dashboard at http://localhost:8501
pytest                                              # run all tests
pytest tests/test_data.py::test_total_orders -v     # run a single test
```

Dependencies are pinned in `requirements.txt`. Recreate the environment with `python3 -m venv venv && source venv/bin/activate && pip install -r requirements.txt`.

## Architecture

The dashboard is split into two layers on purpose:

- **`data.py`** holds all CSV loading and aggregation as plain pandas functions with **no Streamlit import**: `load_data`, `total_sales`, `total_orders`, `sales_by_month`, `sales_by_category`, `sales_by_region`. Each takes a DataFrame and returns a DataFrame or scalar. Because it never imports Streamlit, it is unit-testable by calling the functions directly.
- **`app.py`** is the Streamlit UI. It imports `data.py`, caches the load with `@st.cache_data`, and renders the KPIs and Plotly charts. It does no calculation itself, so the display and the numbers cannot drift apart.

Put any new calculation in `data.py` with a test, and keep `app.py` limited to layout and calls into `data.py`.

`conftest.py` at the repo root exists only so `pytest` adds the root to `sys.path` and tests can `import data`. Without it, pytest's default import mode puts `tests/` on the path instead, and the import fails.

`tests/test_data.py` runs against the real `data/sales-data.csv` (482 records, total sales $116,500.21) and asserts known-good facts rather than using synthetic fixtures.

## Working conventions

- **`TASKS.md` is the milestone board** with `To Do` / `In Progress` / `Done` sections. Milestones are IDed `TASK-1`, `TASK-2`, and so on, derived from the PRD. Move a milestone between sections as you work it.
- **Commit messages start with the milestone ID** (for example `TASK-3: add KPI cards`). Because `TASKS.md` is versioned alongside the code, `git log` then traces each change back to a requirement. This traceability is the point of the tutorial, not an incidental style choice.
- **`docs/` is gitignored on purpose.** It holds Superpowers design specs and implementation plans (`docs/superpowers/specs/`, `docs/superpowers/plans/`), kept local rather than shipped to students. Write specs and plans there, but don't expect to commit them.
- Feature work happens on a branch off `main` and deploys to Streamlit Community Cloud from that branch.

## Environment note

The local interpreter is pyenv's Python 3.11.5, which prints `unsupported hash type blake2b` / `blake2s` tracebacks to stderr on nearly every invocation. These are cosmetic; pip, pytest, and Streamlit all work normally. Don't chase them as a bug.
