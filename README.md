# Nassau Candy Distributor Data Analytics

A beginner-friendly Streamlit dashboard for exploring sales, units, gross profit, factory performance, and product performance in the Nassau Candy Distributor dataset.

## Features
- KPI cards for sales, gross profit, units, and gross margin
- Factory sales and gross-profit charts
- Factory and product summary tables
- Optional Region and Division filters
- Destination summary, where destination columns are available
- CSV download of the factory summary

## Files needed
Place these files in the same folder:
- `app.py`
- `requirements.txt`
- `Nassau Candy Distributor.csv`

**Dataset note:** The app expects the CSV columns used in the internship analysis, including `Product Name`, `Sales`, `Units`, `Gross Profit`, and `Cost`. Keep the original source CSV unchanged. Only upload the dataset to a public repository if you have permission and it contains no confidential information. Otherwise, use a private repository or a sanitized/anonymized dataset.

## Run locally in VS Code
1. Install Python 3.10 or newer.
2. Open this folder in VS Code.
3. In the terminal, run:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   pip install -r requirements.txt
   streamlit run app.py
   ```

4. Streamlit will show a local address, usually `http://localhost:8501`.

## Deploy on Streamlit Community Cloud
1. Push this project to GitHub.
2. Open https://share.streamlit.io/ and sign in with GitHub.
3. Choose **Create app**, select this repository and branch, and set the main file to `app.py`.
4. Deploy and test the live URL.

Do not submit a deployment URL until the app loads successfully.

## Project findings from the completed analysis
- 10,194 records and 18 columns
- Total sales: $141,783.63
- Total gross profit: $93,442.80
- Gross margin: 65.91%
- Total units: 38,654
- Lot's O' Nuts led factory sales and gross profit in the analyzed dataset.
- The Other Factory had the lowest observed gross margin.
- Order-to-ship date differences looked implausibly large; validate date parsing and meaning before presenting shipping duration as a real-world finding.

## Research and publication status
This README and the accompanying paper draft are project documentation, not evidence of peer review, approval, or publication. Do not label the paper as approved or published unless you receive confirmation.
