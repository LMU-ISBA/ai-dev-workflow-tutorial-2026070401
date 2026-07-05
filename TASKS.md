# Tasks

This file tracks all work for the ShopSmart sales dashboard. Move milestones between the sections below as you pick them up and finish them.

## Definition of Done

Every milestone is done only when all of these are true:

- [ ] Its acceptance criteria are met
- [ ] The app runs locally with `streamlit run app.py`
- [ ] Changes are committed with the milestone ID in the message (e.g. `TASK-3: add KPI cards`)

## To Do

## In Progress

### TASK-7: Deploy to Streamlit Community Cloud
Publish the dashboard so stakeholders can reach it from a shareable URL (NFR-5).

- [ ] App is deployed to Streamlit Community Cloud
- [ ] Public URL loads the dashboard without errors
- [ ] The URL is recorded in the README

## Done

### TASK-6: Test and refine
Verify the numbers against the CSV, clean up the layout, and confirm the dashboard is presentable (M6, NFR-2).

Acceptance criteria:

- [x] Displayed values match calculations from the CSV
- [x] Dashboard runs with no errors or warnings
- [x] Labels are clear and the layout is readable

Definition of Done:

- [x] Its acceptance criteria are met
- [x] The app runs locally with `streamlit run app.py`
- [x] Changes are committed with the milestone ID in the message

Commit: `70308af` — TASK-6: finalize tests and polish dashboard layout

### TASK-5: Add category and region breakdowns
Two bar charts: sales by product category and sales by region, each sorted highest to lowest (FR-3, FR-4).

Acceptance criteria:

- [x] Category chart lists all 5 categories, sorted by sales
- [x] Region chart lists all 4 regions, sorted by sales
- [x] Both charts have tooltips with exact values

Definition of Done:

- [x] Its acceptance criteria are met
- [x] The app runs locally with `streamlit run app.py`
- [x] Changes are committed with the milestone ID in the message

Commit: `9477d4f` — TASK-5: add category and region breakdown charts

### TASK-4: Add the sales trend chart
Plot a line chart of sales over time with interactive tooltips (FR-2).

Acceptance criteria:

- [x] Line chart shows sales by date or month
- [x] Hovering a point reveals the exact value

Definition of Done:

- [x] Its acceptance criteria are met
- [x] The app runs locally with `streamlit run app.py`
- [x] Changes are committed with the milestone ID in the message

Commit: `9717950` — TASK-4: add monthly sales trend chart

### TASK-3: Build the KPI cards
Show Total Sales and Total Orders at the top of the dashboard (FR-1).

Acceptance criteria:

- [x] Total Sales displays as currency ($X,XXX,XXX)
- [x] Total Orders shows 482
- [x] Large numbers use thousands separators

Definition of Done:

- [x] Its acceptance criteria are met
- [x] The app runs locally with `streamlit run app.py`
- [x] Changes are committed with the milestone ID in the message

Commit: `84d4203` — TASK-3: add Total Sales and Total Orders KPI cards

### TASK-2: Load the sales data
Read `data/sales-data.csv` with Pandas and parse the date, numeric, and categorical columns (FR-5).

Acceptance criteria:

- [x] All 482 records load with correct data types
- [x] Total sales computed from the CSV is about $116,500 (exact: $116,500.21)

Definition of Done:

- [x] Its acceptance criteria are met
- [x] The app runs locally with `streamlit run app.py`
- [x] Changes are committed with the milestone ID in the message

Commit: `62bd162` — TASK-2: load sales data and compute totals

### TASK-1: Set up the environment and project
Create the Python virtual environment, install Streamlit, Plotly, and Pandas, and scaffold `app.py`.

Acceptance criteria:

- [x] `streamlit run app.py` launches a page without errors
- [x] Dependencies are pinned in `requirements.txt`

Definition of Done:

- [x] Its acceptance criteria are met
- [x] The app runs locally with `streamlit run app.py`
- [x] Changes are committed with the milestone ID in the message

Commit: `440d16c` — TASK-1: set up environment and launchable app
