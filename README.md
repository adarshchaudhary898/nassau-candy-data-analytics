# 🍫 Nassau Candy Distributor — Data Analytics Project

## 📌 About the Project

This project focuses on analyzing sales and shipping data from Nassau Candy Distributor. I worked on this project to practice Python-based data analysis and understand how data can be used to identify business trends and improve decision-making.

The analysis covers factory performance, product sales, gross profit, profit margins, and customer destinations. I also created an interactive dashboard to make the results easier to understand.

## 🌐 Live Dashboard

**[View My Project Dashboard](https://nc-distributers-insights.streamlit.app/)**

The dashboard presents key performance indicators, charts, product performance, destination summaries, and a preview of the dataset.

## 🎯 Project Objectives

- Analyze overall sales, units sold, and gross profit.
- Compare the performance of different factories.
- Identify products with high sales and gross profit.
- Explore customer destinations and factory-to-customer routes.
- Examine shipping date data and identify potential data-quality issues.
- Present the findings through an interactive dashboard.

## 🛠️ Tools & Technologies

- **Python** — data analysis and calculations
- **Pandas** — data cleaning and data manipulation
- **Matplotlib** — data visualization
- **Streamlit** — interactive dashboard
- **GitHub** — source code and project version control

## 📊 Key Results

| Metric | Result |
|---|---:|
| Total records analyzed | 10,194 |
| Unique products | 15 |
| Total units sold | 38,654 |
| Total sales | $141,783.63 |
| Total gross profit | $93,442.80 |
| Overall gross margin | 65.91% |

### Factory Performance

- **Lot's O' Nuts** recorded the highest sales and gross profit among the analyzed factories.
- **Wicked Choccy's** was the second-largest factory by sales.
- The Other Factory had the lowest gross profit margin, indicating an area that may need further investigation.

### Product Analysis

The analysis compares products by sales and gross profit to identify the strongest contributors to overall performance.

### Shipping & Route Analysis

The project summarizes factory-to-customer destinations and examines order and shipping dates. The date calculations require validation before they can be interpreted as actual delivery lead times.

## 📈 Dashboard Features

- Overall business performance KPIs
- Factory sales and gross profit comparisons
- Profit margin analysis
- Product performance charts
- Customer destination summaries
- Dataset preview

## 💻 How to Run the Project Locally

### 1. Clone the repository

```bash
git clone https://github.com/adarshchaudhary898/nassau-candy-data-analytics.git
cd nassau-candy-data-analytics
```

### 2. Install the required libraries

```bash
pip install -r requirements.txt
```

### 3. Add the dataset

Place `Nassau Candy Distributor.csv` in the project folder, alongside `app.py`.

### 4. Run the dashboard

```bash
streamlit run app.py
```

The dashboard should open in your browser.

## ⚠️ Data Quality Note

The date analysis produced unusually large intervals between order and shipping dates. Although the dates could be parsed, their meaning and format need to be confirmed before drawing conclusions about actual shipping delays. Therefore, these values should not be treated as verified delivery performance.

Route distances were not calculated because validated geographic coordinates were not available.

## 📚 What I Learned

Through this project, I practiced working with a real-world-style dataset, using Pandas for analysis, creating charts, comparing business performance, building an interactive Streamlit dashboard, and publishing a project using GitHub and Streamlit Community Cloud.

## 🚀 Future Improvements

- Validate order and shipping dates with the original data source.
- Add geographic coordinates to calculate route distances.
- Explore regional and shipping-mode performance in more detail.
- Add interactive filters for factories, products, and destinations.
- Improve the dashboard with additional business insights.

## 👤 Author

**Adarsh Verma**

MCA Student | Aspiring Data Analyst

[GitHub Profile](https://github.com/adarshchaudhary898)

---

*This project was developed as a learning exercise in data analytics and dashboard development.*
