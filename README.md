# Nassau Candy Distributor Data Analytics

Hi! This is my data analytics project based on the Nassau Candy Distributor dataset. I used Python to explore the data and compare sales and gross profit across products, factories, and destinations.

## What I wanted to learn

The main goal was to turn the raw CSV data into summaries that are easier to understand. I looked at:

- Total sales, units sold, gross profit, and gross margin
- Sales and profit by factory
- Product performance
- Factory-to-city/state summaries
- Basic data quality checks

## Tools I used

- **Python** for analysis
- **pandas** for reading and summarizing the CSV
- **Matplotlib** for charts
- **openpyxl / Excel** for the formatted workbook
- **Streamlit** for the web dashboard
- **VS Code** for writing and running the code

## Main results

The dataset I analyzed has **10,194 rows** and **18 columns**.

| Metric | Result |
|---|---:|
| Total units | 38,654 |
| Total sales | $141,783.63 |
| Total gross profit | $93,442.80 |
| Overall gross margin | 65.91% |

In my factory comparison, **Lot's O' Nuts** had the highest recorded sales and gross profit. **The Other Factory** had the lowest recorded gross margin, so its product mix, pricing, and cost data could be checked in more detail.

These are descriptive findings from this dataset. They do not explain the reasons behind a factory's performance by themselves.

## Data quality note

I checked the dataset for missing values and exact duplicate rows. The checks reported no missing values and no exact duplicate rows.

I also looked at the Order Date and Ship Date fields. The calculated differences were much larger than normal shipping times (median around 1,274 days), so I have not treated them as confirmed delivery delays. The date format and meaning of these fields should be verified before using them for shipping-performance conclusions.

## Run the dashboard on your computer

### 1. Get the project files

Download or clone this repository and open the project folder in VS Code.

The dashboard expects a file named `Nassau Candy Distributor.csv` in the same folder as `app.py`.

**Please only use or share the dataset if you have permission to do so.** If the data is not allowed to be public, keep it out of a public repository and use an approved private data source or a sanitized sample.

### 2. Install the packages

Open the VS Code terminal in the project folder and run:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Start Streamlit

```bash
streamlit run app.py
```

Streamlit should provide a local URL to open the dashboard in your browser.

## Project files

- `app.py` — Streamlit dashboard
- `requirements.txt` — Python packages needed by the dashboard
- `README.md` — project notes and setup instructions

Other analysis outputs, charts, and reports may be stored separately depending on which project files are included in the repository.

## What I learned

This project helped me practise loading CSV data, checking data quality, grouping records, calculating business metrics, making charts, and presenting results in a dashboard. I also learned that it is important to mention data limitations instead of assuming every calculated value is meaningful.

## Next steps

- Confirm the correct interpretation of the date fields
- Review the low recorded margin for The Other Factory in more detail
- Add more filters or trends after validating the relevant data
- Keep the dashboard and project documentation updated as the analysis improves

---
This is a learning and descriptive analytics project. The results depend on the supplied dataset and the product-to-factory mapping used in the analysis.
