# Google Cloud ETL Pipeline

**Author:** Pedro Siqueira

## Project Overview

This repository contains a production-ready ETL (Extract, Transform, Load) pipeline built with Python and Google Cloud Platform. The pipeline demonstrates enterprise-level data engineering capabilities by processing sales data from CSV files through to analytics-ready tables in BigQuery.

## Technical Architecture

The pipeline follows modern cloud-native design principles:

```
Source Data (CSV) → Python Processing → Cloud Storage → BigQuery → Business Analytics
```

**Key Components:**
- **Extraction Layer**: Pandas-based CSV processing with data validation
- **Transformation Layer**: Business logic implementation and data quality checks  
- **Storage Layer**: Google Cloud Storage for data lake functionality
- **Analytics Layer**: BigQuery data warehouse for SQL-based analysis
- **Security Layer**: Service account authentication with IAM controls

## Technologies and Tools

- **Python 3.x** - Core development language
- **Pandas** - Data manipulation and transformation
- **Google Cloud Storage** - Scalable object storage for data lake
- **Google BigQuery** - Serverless data warehouse platform
- **Google Cloud IAM** - Identity and access management
- **Git** - Version control and collaboration

## Features Implemented

**Data Processing:**
- Automated CSV file ingestion with schema validation
- Data transformation including calculated fields and date parsing
- Comprehensive error handling and logging throughout pipeline
- Data quality validation with null value detection

**Cloud Integration:**
- Dynamic bucket creation in Google Cloud Storage
- Automated BigQuery dataset and table provisioning
- Service account authentication for secure cloud access
- Timestamped file naming for version control

**Analytics Capabilities:**
- SQL-based business intelligence queries
- Regional sales performance analysis
- Product performance ranking and metrics
- Real-time data availability for business decisions

## Business Results

The pipeline processes sales transactions and generates actionable insights:

**Regional Performance Analysis:**
- Europe: $2,909.94 total revenue (highest performing market)
- North America: $2,569.83 total revenue  
- Asia: $1,869.92 total revenue

**Product Performance Metrics:**
- Top revenue generator: Laptop ($2,499.99 from 2 orders)
- High-value single transactions: Sofa ($899.99), Smartphone ($799.99)
- Multi-unit sales optimization: Monitor and Desk Chair categories

## Implementation Details

**File Structure:**
```
pipeline_to_GC.py          # Main ETL pipeline implementation
README.md                  # Project documentation
```

**Pipeline Execution:**
```bash
python3 pipeline_to_GC.py
```

**Prerequisites:**
- Python 3.x with pandas library
- Google Cloud Platform account with billing enabled
- Service account credentials (JSON file)
- BigQuery and Cloud Storage APIs enabled

## Skills Demonstrated

**Data Engineering:**
- ETL pipeline design and implementation
- Data warehouse architecture and modeling
- Cloud-native application development
- Production-ready error handling and logging

**Google Cloud Platform:**
- BigQuery data warehouse implementation
- Cloud Storage integration for data lake architecture
- IAM security configuration and service accounts
- Serverless computing and auto-scaling capabilities

**Software Development:**
- Object-oriented programming with Python
- Professional code documentation and commenting
- Git version control and collaborative development
- Enterprise software development practices

## Performance and Scalability

The pipeline architecture supports:
- Horizontal scaling through cloud-native services
- Sub-second query response times in BigQuery
- Automatic schema detection and table provisioning
- Zero-maintenance serverless infrastructure

## Future Enhancements

Potential improvements for production deployment:
- Apache Airflow integration for workflow orchestration
- Real-time streaming data processing with Pub/Sub
- Advanced monitoring and alerting with Cloud Operations
- Multi-environment deployment with Infrastructure as Code

## Contact

Pedro Siqueira  
Data Engineer | Python Developer | Cloud Architect

This project demonstrates practical experience with modern data engineering tools and cloud platforms, suitable for enterprise-level data processing requirements.