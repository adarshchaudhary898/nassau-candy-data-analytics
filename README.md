# NC Distributors Insights — Factory-to-Customer Route Analysis

**Developed by Adarsh Verma**  
MCA Student | Data Analytics Project

<p align="center">
  <a href="https://nc-distributers-insights.streamlit.app/">
    <img src="https://img.shields.io/badge/Live-Dashboard-brightgreen?style=for-the-badge&logo=streamlit" alt="Live Dashboard">
  </a>
  <a href="https://github.com/adarshchaudhary898/nassau-candy-data-analytics">
    <img src="https://img.shields.io/badge/GitHub-Repository-black?style=for-the-badge&logo=github" alt="GitHub Repository">
  </a>
</p>

## Live Demo

**Explore the interactive dashboard:**  
https://nc-distributers-insights.streamlit.app/

**Source Code:**  
https://github.com/adarshchaudhary898/nassau-candy-data-analytics

## About the Project

NC Distributors Insights is a Python-based data analytics project that examines factory-to-customer shipping routes using the Nassau Candy Distributor dataset. It explores sales, profitability, order-to-ship intervals, shipping modes and geographic patterns through an interactive Streamlit dashboard.

The project aims to make route-related data easier to explore and help identify patterns that may warrant further investigation.

## Key Features

- Factory-wise sales, gross profit and profit-margin analysis
- Factory-to-customer state and region route summaries
- Fastest and slowest observed order-to-ship intervals
- Relative route-efficiency scoring and threshold flags
- US state-level map using approximate state centroids
- Shipping-mode comparisons
- Order-level route drill-down
- Interactive filters for dates, regions, states, shipping modes, factories and thresholds
- Data-quality checks and downloadable CSV summaries

## Technology Stack

- **Python** — data processing and application logic
- **Pandas** — data cleaning and analysis
- **Streamlit** — interactive dashboard
- **Plotly** — interactive visualizations
- **GitHub** — source-code version control
- **Streamlit Community Cloud** — deployment

## Repository Structure

```text
nassau-candy-data-analytics/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .devcontainer/
└── Nassau Candy Distributor.csv
```

The dataset should only be included in the repository if you have permission to share it publicly. The application and documentation may also be used with a permitted local copy of the dataset.

## Run the Project Locally

### Prerequisites

- Python installed on your computer
- Visual Studio Code or another Python editor
- A permitted copy of `Nassau Candy Distributor.csv`

### Installation

1. Clone or download this repository.
2. Open the project folder in VS Code.
3. Open the terminal and create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

4. Activate the environment in PowerShell:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

5. Install dependencies:

   ```powershell
   python -m pip install -r requirements.txt
   ```

6. Place the CSV beside `app.py` if it is not already available there.
7. Start the dashboard:

   ```powershell
   python -m streamlit run app.py
   ```

8. Open the local URL shown in the terminal, usually `http://localhost:8501`.

## Data Protection

The application reads `Nassau Candy Distributor.csv` and performs its analysis in memory. It is designed not to overwrite the original source CSV.

Keep a backup of the original dataset. Do not publish confidential or restricted data; use a private repository or an authorised, sanitised dataset when required.

## Important Analytical Limitations

The source analysis produced an average order-to-ship interval of approximately **1,320.84 days** and a median of approximately **1,274 days**. These values are unusually large for normal shipping and require validation of the source dates and business definitions.

- The interval represents the difference between order date and ship date, not confirmed delivery time.
- The dataset does not include a confirmed delivery date or a separate shipping-charge field.
- The dashboard cannot independently establish actual delivery delays or shipping-cost savings.
- The state map uses approximate state centroids rather than exact customer coordinates.
- Relative route-efficiency scores are analytical indicators, not verified operational performance measurements.

Interpret these findings cautiously and validate the underlying data before drawing business conclusions.

## Verification Checklist

- [ ] CSV loads with the expected columns.
- [ ] Sales and row totals reconcile with the source data.
- [ ] Date parsing has been validated against original records.
- [ ] Filters update the displayed metrics consistently.
- [ ] State names and abbreviations map correctly.
- [ ] CSV downloads open correctly.
- [ ] The local and deployed dashboards run without errors.

## Author

**Adarsh Verma**  
MCA Student | Aspiring Data Analyst

- **GitHub:** https://github.com/adarshchaudhary898
- **Project Repository:** https://github.com/adarshchaudhary898/nassau-candy-data-analytics
- **Live Dashboard:** https://nc-distributers-insights.streamlit.app/

---

*This project was developed for learning and demonstrating data analytics, interactive visualization and exploratory shipping-route analysis.*
