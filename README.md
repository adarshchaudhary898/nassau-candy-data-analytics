# NC Distributors Insights — Factory-to-Customer Route Analysis

Live dashboard: https://nc-distributers-insights.streamlit.app/

## What this project includes
- Factory and product sales/profit overview
- Factory → customer state/region route aggregation
- Fastest and slowest observed order-to-ship intervals
- Relative route efficiency score and delay-threshold flags
- State-level US map using approximate state centroids
- Ship-mode comparisons
- Order-level route drill-down
- Interactive date, region, state, ship-mode, factory and threshold filters
- Data-quality checks and CSV downloads
- Research paper draft

## Files
- `app.py` — Streamlit application
- `requirements.txt` — Python dependencies
- `research_paper_draft.md` — draft research paper
- `Nassau Candy Distributor.csv` — source dataset, supplied separately by the project owner

## Protect the original CSV
The app reads `Nassau Candy Distributor.csv` from the same folder as `app.py`. It does not write to or overwrite the source file. Derived date columns are created in memory only. Keep a backup before making changes.

The starter ZIP intentionally does not contain the source dataset. Place your existing CSV beside `app.py`. For public GitHub deployment, upload the data only if you have permission and it contains no confidential information. Otherwise use a private repository or a permitted sanitized dataset.

## Run locally (Windows / VS Code)
1. Extract this ZIP into a new folder, leaving your existing project untouched.
2. Copy your original `Nassau Candy Distributor.csv` into the extracted folder.
3. Open the extracted folder in VS Code.
4. Open Terminal and run:

   ```powershell
   py -m venv .venv
   .venv\Scripts\Activate.ps1
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   streamlit run app.py
   ```

   If PowerShell blocks activation, use Command Prompt and run `.venv\Scripts\activate.bat`, then continue.

5. Open the local URL Streamlit prints (usually `http://localhost:8501`).

## Deploy on Streamlit Community Cloud
1. Commit `app.py`, `requirements.txt`, and documentation to the intended GitHub repository.
2. Ensure the CSV is available to the deployed app through a permitted, secure approach. Do not publish confidential data.
3. In Streamlit Community Cloud, select the repository and branch, set the main file path to `app.py`, then deploy.
4. Check the app logs if dependency installation or file loading fails.
5. Verify filters, route summaries, map and downloads in the deployed app.

## Important data interpretation limitation
The supplied project analysis found an average order-to-ship date difference of about 1,320.84 days and median of about 1,274 days. Those values are implausibly large for normal shipping. The dashboard labels the measure **order-to-ship interval**, not confirmed transit or delivery time, and flags unusually long intervals for investigation. Confirm source date format and business definitions before presenting these values as actual shipping delays.

The data does not contain a confirmed delivery date or a separate shipping-charge field. Therefore this dashboard cannot prove actual delivery lateness, route distance to customer addresses, or shipping-cost savings. The state map uses approximate state centroids, not customer coordinates.

## Suggested verification checklist
- [ ] CSV loads and expected columns are present
- [ ] Total rows and sales reconcile with the source analysis
- [ ] Date parsing has been checked against original source rows
- [ ] Filters change all displayed metrics consistently
- [ ] State names/abbreviations map as expected
- [ ] CSV downloads open correctly
- [ ] Local and deployed apps both load without errors
