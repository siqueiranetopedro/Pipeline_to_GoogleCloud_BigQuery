# Complete Data Pipeline: CSV to Looker Studio via Google Cloud

![Pipeline Flow](https://img.shields.io/badge/Pipeline-CSV%20→%20Python%20→%20BigQuery%20→%20Looker%20Studio-blue)
![Status](https://img.shields.io/badge/Status-Complete-green)
![Python](https://img.shields.io/badge/Python-3.x-blue)
![GCP](https://img.shields.io/badge/Google%20Cloud-BigQuery-orange)

## Project Overview

This project demonstrates a complete end-to-end data pipeline that transforms raw CSV data into interactive business visualizations. The pipeline automates the entire process from local data files to cloud-based analytics dashboards.

## Pipeline Architecture

```
CSV File (Desktop) 
    ↓
Python ETL Script 
    ↓
Google Cloud Storage 
    ↓
BigQuery Data Warehouse 
    ↓
Looker Studio Dashboard
```

## Dashboard Preview

<img width="2398" height="1658" alt="image" src="https://github.com/user-attachments/assets/756744f3-60df-4158-83d2-a6f59e2a201d" />


*Live interactive dashboard showing sales data across regions with geographic visualization and detailed product analytics*

## Data Flow Process

### 1. Data Source
- **Input**: `sample_sales_data.csv` stored locally on desktop
- **Format**: Structured sales data with customer regions, products, quantities, and sales amounts

### 2. Python ETL Pipeline (`pipeline_to_GC.py`)
- **Data Cleaning**: Handles missing values, data type conversions
- **Data Transformation**: Aggregates and calculates business metrics
- **Cloud Upload**: Securely uploads processed data to Google Cloud
- **BigQuery Integration**: Creates tables and loads data into BigQuery

### 3. BigQuery Data Warehouse
- **Storage**: Scalable cloud data warehouse
- **Processing**: SQL queries for data analysis and aggregation
- **Optimization**: Partitioned tables for improved performance

### 4. Looker Studio Visualization
- **Connection**: Direct integration with BigQuery
- **Dashboards**: Interactive charts, maps, and tables
- **Analytics**: Real-time business insights and KPIs

## Final Dashboard Features

The completed Looker Studio dashboard includes:

- **Geographic Sales Map**: Visual representation of sales by region
- **Product Performance**: Category and product-level analysis
- **Data Tables**: Detailed breakdowns with quantities and values
- **Regional Insights**: North America, Europe, Asia performance metrics

**Live Dashboard**: [View in Looker Studio](https://lookerstudio.google.com/u/0/reporting/bb31005f-b077-4992-ab4d-2e58d484c680/page/fMDcF/edit)

## Technologies Used

| Component | Technology | Purpose |
|-----------|------------|---------|
| **ETL Processing** | Python 3.x | Data cleaning and transformation |
| **Cloud Storage** | Google Cloud Storage | Scalable file storage |
| **Data Warehouse** | BigQuery | Analytics and querying |
| **Visualization** | Looker Studio | Interactive dashboards |
| **Authentication** | Google Cloud IAM | Secure access management |

## Project Structure

```
Pipeline_to_GoogleCloud/
├── pipeline_to_GC.py           # Main ETL script
├── pedro-credentials.json      # GCP service account credentials
├── sample_sales_data.csv       # Source data file
├── simple_etl_pipeline.py      # Alternative ETL implementation
└── README.md                   # Project documentation
```

## How to Run

### Prerequisites
```bash
pip install google-cloud-bigquery google-cloud-storage pandas
```

### Execution
```bash
python pipeline_to_GC.py
```

### Configuration
1. Set up Google Cloud Project
2. Enable BigQuery and Cloud Storage APIs
3. Create service account and download credentials
4. Update file paths in the script

## Data Schema

### Input CSV Structure
```
customer_region | product | quantity | sales_amount | category
North America  | Laptop  | 1        | 1200        | Electronics
Europe         | Sofa    | 1        | 899.99      | Furniture
Asia           | Phone   | 4        | 79.99       | Electronics
```

### BigQuery Output Schema
```sql
CREATE TABLE sales_data (
  customer_region STRING,
  category STRING,
  product STRING,
  quantity INT64,
  sales_amount FLOAT64,
  total_value FLOAT64
);
```

## Business Value

### Key Metrics Delivered
- **Regional Performance**: Identify top-performing geographic markets
- **Product Analytics**: Track best-selling products and categories
- **Revenue Insights**: Calculate total values and profit margins
- **Trend Analysis**: Monitor sales patterns over time

### Business Impact
- **Automated Reporting**: Eliminated manual data processing
- **Real-time Insights**: Live dashboard updates
- **Scalable Architecture**: Cloud-based solution grows with data
- **Cost Effective**: Pay-per-use cloud infrastructure

## Related Resources

- [Google Cloud BigQuery Documentation](https://cloud.google.com/bigquery/docs)
- [Looker Studio Help Center](https://support.google.com/looker-studio)
- [Python Pandas Documentation](https://pandas.pydata.org/docs/)

## Author

**Pedro Siqueira**
- GitHub: [@siqueiranetopedro](https://github.com/siqueiranetopedro)
- Project: [Pipeline_to_GoogleCloud](https://github.com/siqueiranetopedro/Pipeline_to_GoogleCloud)

---

*This project demonstrates the complete journey from raw data to actionable business insights using modern cloud technologies and best practices in data engineering.*
