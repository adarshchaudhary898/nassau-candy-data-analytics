# Sales and Gross-Profit Analysis of a Candy Distributor Dataset Using Python

**Author:** [Your Name]  
**Institution/Internship:** [Add institution or internship organization]  
**Status:** Draft project paper — not approved or published

## Abstract
This project applies exploratory data analysis to a distributor sales dataset to examine sales, units sold, gross profit, gross margin, product performance, and factory-level performance. Python, pandas, Matplotlib, and spreadsheet tools were used to validate the dataset, summarize key performance indicators, and present results through tables, charts, and a dashboard prototype. The analyzed dataset contains 10,194 records and 18 columns, with no missing values or exact duplicate rows detected in the initial quality checks. Total sales were $141,783.63 and total gross profit was $93,442.80, producing an aggregate gross margin of approximately 65.91%. Lot's O' Nuts contributed the largest share of sales and gross profit among the mapped factories. The analysis also identified a data-quality concern: order-to-ship date differences were implausibly large under the date interpretation tested. Consequently, shipping-duration conclusions should not be treated as validated until the date format and field semantics are confirmed. The project demonstrates how descriptive analytics can convert transaction-level records into business summaries while documenting limitations and avoiding unsupported causal claims.

**Keywords:** data analytics, Python, pandas, sales analysis, gross profit, dashboard, data quality

## 1. Introduction
Organizations use transaction data to monitor sales, profitability, product performance, and operational patterns. Raw records, however, are difficult to interpret without systematic cleaning, aggregation, and visualization. This project analyzes a candy distributor dataset to produce clear summaries for business review. The emphasis is on descriptive analysis rather than causal inference or forecasting.

## 2. Objectives
1. Inspect dataset structure and quality.
2. Calculate sales, units, gross profit, and gross margin.
3. Compare mapped factories and products.
4. Explore shipping-mode and destination summaries where the available fields permit.
5. Present the results in charts, tables, and a dashboard.
6. Document assumptions and data limitations.

## 3. Dataset
The source file, `Nassau Candy Distributor.csv`, contains 10,194 rows and 18 columns. Fields include order identifiers and dates, shipping mode, customer and destination information, division, region, product identifiers and names, sales, units, gross profit, and cost. The original source file should be preserved unchanged. Any transformed dataset used for analysis should be saved separately.

## 4. Tools and Methodology
Python was used for data processing and analysis. pandas supported loading, validation, grouping, and aggregation. Matplotlib supported charts, while Excel and a Word report supported presentation. The workflow consisted of:
1. Load the CSV and inspect its shape and columns.
2. Check missing values and exact duplicate rows.
3. convert numeric measures to numeric types and inspect invalid values.
4. Map products to factories using the project’s supplied mapping.
5. Calculate totals and grouped metrics.
6. Build charts and summary exports.
7. Review results and document limitations.

## 5. Results
### 5.1 Overall metrics
| Metric | Result |
|---|---:|
| Records | 10,194 |
| Columns | 18 |
| Units | 38,654 |
| Total sales | $141,783.63 |
| Total gross profit | $93,442.80 |
| Aggregate gross margin | 65.91% |
| Missing values detected | 0 |
| Exact duplicate rows detected | 0 |

Gross margin is calculated as total gross profit divided by total sales, multiplied by 100.

### 5.2 Factory performance
| Factory | Records | Units | Sales | Gross profit | Gross margin |
|---|---:|---:|---:|---:|---:|
| Lot's O' Nuts | 5,692 | 21,412 | $76,340.15 | $52,771.05 | 69.13% |
| Wicked Choccy's | 4,152 | 15,863 | $55,352.75 | $36,053.57 | 65.13% |
| Secret Factory | 217 | 884 | $8,587.50 | $4,344.70 | 50.59% |
| The Other Factory | 100 | 388 | $1,282.25 | $152.25 | 11.87% |
| Sugar Shack | 33 | 107 | $220.98 | $121.23 | 54.86% |

Lot's O' Nuts accounted for approximately 53.84% of total sales and had the largest gross-profit contribution in the summarized data. The Other Factory had the lowest observed gross margin; this is a signal for further review, not proof of a particular cause.

### 5.3 Product performance
Wonka Bar - Triple Dazzle Caramel recorded the highest product sales at $28,485. Wonka Bar -Scrumdiddlyumptious recorded the highest product gross profit at $19,357.50. Fun Dip had the lowest recorded sales at $12. These results are descriptive and depend on the product-to-factory mapping used in the project.

### 5.4 Route and destination analysis
The dataset supported a summary of factory-to-city/state combinations. There were 1,278 unique mapped factory-destination routes. The highest route by record count was Lot's O' Nuts to New York City, NY, with 533 records, $7,184.18 in sales, and $4,965.68 in gross profit. Because destination coordinates were not provided, route distances were not calculated.

### 5.5 Shipping-date limitation
When dates were interpreted using the tested day-month-year format, all date pairs parsed, but the order-to-ship differences were implausibly large: median 1,274 days and mean approximately 1,320.84 days. This suggests the date format, source semantics, or data itself requires verification. These values must not be presented as actual delivery delays until confirmed with the data owner.

## 6. Business Insights and Recommendations
- Review the practices and product mix associated with Lot's O' Nuts, which leads the analyzed dataset in sales and gross profit; do not assume the same performance will persist without further analysis.
- Review The Other Factory's low observed gross margin by validating cost and pricing data and examining product-level results.
- Investigate low-volume factory results cautiously because small record counts can make percentages unstable.
- Validate order and ship dates before using shipping-duration metrics.
- Refresh the dashboard when new, verified data becomes available.

## 7. Limitations
The analysis is descriptive and does not establish causal relationships. Factory assignment relies on the mapping supplied for this project. No destination coordinates were available for distance calculations. Date differences appear implausible and need validation. Results describe this dataset and should not be generalized beyond it without further evidence.

## 8. Conclusion
The project demonstrates a reproducible workflow for checking, summarizing, and visualizing distributor sales data. It produces key performance indicators and factory/product comparisons that are easier to interpret than raw transaction rows. Its most important quality-control finding is the implausible order-to-ship date interval, which shows why validation and transparent limitations are essential parts of data analytics.

## References
1. pandas documentation, https://pandas.pydata.org/docs/
2. Matplotlib documentation, https://matplotlib.org/stable/
3. Streamlit documentation, https://docs.streamlit.io/

## Publication statement
This is a draft project paper. It has not been represented as peer-reviewed, approved, accepted, or published. Add the actual repository and deployment URLs only after they exist and have been tested.
