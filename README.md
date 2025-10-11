# Google Cloud ETL Pipeline

**Author:** Pedro Siqueira

## About This Project

I built this ETL pipeline to learn how to work with Google Cloud Platform and process real data in the cloud. This project helped me understand how modern data systems work and how to build something that can handle business data at scale.

## What It Does

The pipeline takes sales data from CSV files and processes it through Google Cloud:

```
CSV File → Python Processing → Cloud Storage → BigQuery → Analytics
```

**The process:**
1. **Extract** - Reads data from CSV files and validates it
2. **Transform** - Cleans the data and adds calculated fields using pandas
3. **Load** - Saves data to Google Cloud Storage and BigQuery
4. **Analyze** - Runs SQL queries to get business insights

## Tools I Used

- **Python** - Main programming language for the pipeline
- **Pandas** - For cleaning and transforming the data
- **Google Cloud Storage** - To store the processed files
- **BigQuery** - Google's data warehouse for running queries
- **Google Cloud IAM** - For secure authentication

## What I Learned

**Working with Cloud Services:**
- How to set up and use Google Cloud Storage buckets
- Creating and managing BigQuery datasets and tables
- Setting up proper authentication with service accounts
- Handling errors when working with cloud APIs

**Data Processing:**
- Reading and validating CSV data with pandas
- Adding business logic to transform raw data
- Creating automated data quality checks
- Building reusable code that handles different data sources

## How to Run It

**What you need:**
- Python 3.x with pandas installed
- A Google Cloud account
- Service account credentials (JSON file)
- BigQuery and Cloud Storage enabled in your project

## Code Structure

The main file `pipeline_to_GC.py` contains:
- `CloudETLPipeline` class that handles all the processing
- Methods for extracting, transforming, and loading data
- Error handling for when things go wrong
- SQL queries for generating business reports

## Next Steps

Things I want to add in the future:
- Schedule the pipeline to run automatically
- Add more data sources like APIs or databases
- Create better monitoring and alerts
- Build a dashboard to visualize the results

## Connection

This project builds on my previous work with Excel and APIs that you can see here: https://github.com/siqueiranetopedro/Pipelines_Excel-API

Feel free to look at the code and reach out if you have questions about how it works.

---

**Pedro Siqueira**  
Learning data engineering and cloud technologies
