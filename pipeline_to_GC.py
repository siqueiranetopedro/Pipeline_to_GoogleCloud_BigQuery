# ETL Pipeline to Google Cloud Platform

import os  # For environment variable management
import pandas as pd  # For data manipulation and processing
from google.cloud import storage, bigquery  # Google Cloud client libraries
from datetime import datetime  # For timestamping files and operations
import json  # For handling JSON data structures

class CloudETLPipeline:
    
    
    def __init__(self, credentials_file):
        """Initialize the pipeline with Google Cloud credentials"""
        print("Initializing Google Cloud ETL Pipeline...")
        
        # Set environment variable for Google Cloud authentication
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_file
        
        # Define project configuration
        self.project_id = "symbolic-axe-474621-e8"  # Google Cloud project identifier
        self.bucket_name = f"pedro-etl-{datetime.now().strftime('%Y%m%d')}"  # Unique bucket name with date
        
        # Initialize Google Cloud service clients
        self.storage_client = storage.Client(project=self.project_id)  # Cloud Storage client for file operations
        self.bigquery_client = bigquery.Client(project=self.project_id)  # BigQuery client for data warehouse operations
        
        print(f"Connected to Google Cloud project: {self.project_id}")
    
    def extract_data(self, file_path):
        """Extract data from CSV file and perform initial validation"""
        print("Starting data extraction phase...")
        
        # Read CSV file into pandas DataFrame
        df = pd.read_csv(file_path)  # Load data from file into memory
        print(f"Successfully loaded {len(df)} rows from {file_path}")
        
        # Display basic information about the dataset
        print(f"Dataset shape: {df.shape}")  # Show number of rows and columns
        print(f"Columns: {list(df.columns)}")  # List all column names
        
        return df  # Return DataFrame for next processing step
    
    def transform_data(self, df):
        """Transform and enrich the data with business logic"""
        print("Starting data transformation phase...")
        
        # Add calculated fields for business analysis
        df['month'] = pd.to_datetime(df['date']).dt.strftime('%Y-%m')  # Extract month from date for time series analysis
        df['total_value'] = df['sales_amount'] * df['quantity']  # Calculate total transaction value
        
        # Data quality validation
        null_counts = df.isnull().sum()  # Check for missing values in each column
        if null_counts.sum() > 0:  # If any null values found
            print(f"Warning: Found {null_counts.sum()} null values")
        
        # Generate summary statistics for validation
        total_sales = df['sales_amount'].sum()  # Calculate total sales amount
        total_transactions = len(df)  # Count total number of transactions
        print(f"Data validation: {total_transactions} transactions totaling ${total_sales:,.2f}")
        
        return df  # Return transformed DataFrame
    
    def load_to_storage(self, df):
        """Upload processed data to Google Cloud Storage"""
        print("Loading data to Cloud Storage...")
        
        try:
            # Create or get storage bucket
            bucket = self.storage_client.bucket(self.bucket_name)  # Reference to storage bucket
            if not bucket.exists():  # Check if bucket already exists
                bucket = self.storage_client.create_bucket(self.bucket_name, location="US")  # Create new bucket in US region
                print(f"Created new storage bucket: {self.bucket_name}")
            else:
                print(f"Using existing storage bucket: {self.bucket_name}")
            
            # Generate unique filename with timestamp
            blob_name = f"sales_data_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"  # Create timestamped filename
            blob = bucket.blob(blob_name)  # Create blob reference for file upload
            
            # Upload DataFrame as CSV to cloud storage
            csv_data = df.to_csv(index=False)  # Convert DataFrame to CSV string format
            blob.upload_from_string(csv_data, content_type='text/csv')  # Upload CSV data to cloud
            print(f"Successfully uploaded file: {blob_name}")
            
        except Exception as e:  # Handle any upload errors
            print(f"Error uploading to Cloud Storage: {e}")
            raise  # Re-raise exception to stop pipeline
    
    def load_to_bigquery(self, df):
        """Load data into BigQuery data warehouse for analytics"""
        print("Loading data to BigQuery data warehouse...")
        
        try:
            # Create or get BigQuery dataset
            dataset_id = "pedro_etl_demo"  # Dataset name for organizing tables
            dataset_ref = self.bigquery_client.dataset(dataset_id)  # Reference to dataset
            
            try:
                dataset = self.bigquery_client.get_dataset(dataset_ref)  # Try to get existing dataset
                print(f"Using existing BigQuery dataset: {dataset_id}")
            except:  # If dataset doesn't exist
                dataset = bigquery.Dataset(dataset_ref)  # Create new dataset object
                dataset.location = "US"  # Set geographic location for data storage
                dataset = self.bigquery_client.create_dataset(dataset)  # Create dataset in BigQuery
                print(f"Created new BigQuery dataset: {dataset_id}")
            
            # Create table and load data
            table_id = "sales_data"  # Table name for storing sales data
            table_ref = dataset_ref.table(table_id)  # Reference to specific table
            
            # Configure data loading job
            job_config = bigquery.LoadJobConfig(  # Set up load job parameters
                write_disposition="WRITE_TRUNCATE",  # Replace existing data completely
                autodetect=True  # Automatically detect schema from data
            )
            
            # Execute data loading job
            job = self.bigquery_client.load_table_from_dataframe(df, table_ref, job_config=job_config)  # Start load job
            job.result()  # Wait for job completion and check for errors
            
            print(f"Successfully loaded {len(df)} rows to BigQuery table: {table_id}")
            
        except Exception as e:  # Handle any BigQuery errors
            print(f"Error loading to BigQuery: {e}")
            raise  # Re-raise exception to stop pipeline
    
    def run_analytics(self):
        """Execute business intelligence queries on the loaded data"""
        print("Running analytics queries...")
        
        # Define business intelligence queries
        queries = [
            {
                "name": "Top Performing Products",  # Query description
                "sql": """
                SELECT 
                    product,  -- Product name
                    SUM(total_value) as total_sales,  -- Total revenue per product
                    COUNT(*) as order_count  -- Number of orders per product
                FROM `symbolic-axe-474621-e8.pedro_etl_demo.sales_data`  -- Fully qualified table name
                GROUP BY product  -- Group results by product
                ORDER BY total_sales DESC  -- Sort by highest sales first
                LIMIT 5  -- Return only top 5 products
                """
            },
            {
                "name": "Regional Sales Performance",  # Query description
                "sql": """
                SELECT 
                    customer_region,  -- Geographic region
                    SUM(total_value) as total_sales,  -- Total revenue per region
                    AVG(sales_amount) as avg_order_value  -- Average order value per region
                FROM `symbolic-axe-474621-e8.pedro_etl_demo.sales_data`  -- Source table
                GROUP BY customer_region  -- Group by geographic region
                ORDER BY total_sales DESC  -- Sort by highest revenue first
                """
            }
        ]
        
        # Execute each analytics query
        for query in queries:  # Iterate through all defined queries
            try:
                print(f"\nExecuting query: {query['name']}")
                result = self.bigquery_client.query(query['sql']).result()  # Run SQL query and get results
                
                # Display query results
                for row in result:  # Iterate through each result row
                    if query['name'] == "Top Performing Products":  # Format product analysis results
                        print(f"  {row.product}: ${row.total_sales:,.2f} revenue ({row.order_count} orders)")
                    else:  # Format regional analysis results
                        print(f"  {row.customer_region}: ${row.total_sales:,.2f} revenue (avg order: ${row.avg_order_value:,.2f})")
                        
            except Exception as e:  # Handle query execution errors
                print(f"Error executing query '{query['name']}': {e}")
    
    def run_pipeline(self, data_file_path):
        """Execute the complete ETL pipeline process"""
        print("Starting ETL pipeline execution...")
        print("=" * 50)
        
        try:
            # Step 1: Extract data from source
            raw_data = self.extract_data(data_file_path)  # Load data from CSV file
            
            # Step 2: Transform and validate data
            processed_data = self.transform_data(raw_data)  # Apply business logic and validation
            
            # Step 3: Load to cloud storage (data lake)
            self.load_to_storage(processed_data)  # Upload to Google Cloud Storage
            
            # Step 4: Load to data warehouse
            self.load_to_bigquery(processed_data)  # Insert into BigQuery for analytics
            
            # Step 5: Generate business insights
            self.run_analytics()  # Execute analytical queries
            
            print("\nETL pipeline completed successfully")
            print(f"Data available at: https://console.cloud.google.com/bigquery?project={self.project_id}")
            
            return True  # Indicate successful pipeline execution
            
        except Exception as e:  # Handle any pipeline failures
            print(f"Pipeline execution failed: {e}")
            return False  # Indicate pipeline failure

def main():
    """Main function to initialize and run the ETL pipeline"""
    print("Pedro's ETL Pipeline for Google Cloud Platform")
    print("=" * 50)
    
    # Define file paths and configuration
    credentials_file = "/Users/pedrosiqueira/Desktop/pedro-credentials.json"  # Path to service account credentials
    data_file = "sample_sales_data.csv"  # Source data file
    
    # Validate that required files exist
    if not os.path.exists(credentials_file):  # Check if credentials file is available
        print(f"Error: Credentials file not found at {credentials_file}")
        print("Please ensure the Google Cloud service account JSON file is in the correct location")
        return
    
    if not os.path.exists(data_file):  # Check if data file is available
        print(f"Error: Data file not found: {data_file}")
        print("Please ensure the source data file exists in the current directory")
        return
    
    try:
        # Initialize and execute pipeline
        pipeline = CloudETLPipeline(credentials_file)  # Create pipeline instance with credentials
        success = pipeline.run_pipeline(data_file)  # Execute complete ETL process
        
        if success:  # If pipeline executed successfully
            print("\nPipeline execution completed successfully")
            print("Data is now available in Google Cloud for analysis and reporting")
        else:  # If pipeline failed
            print("\nPipeline execution failed - check error messages above")
        
    except Exception as e:  # Handle any initialization errors
        print(f"Failed to initialize pipeline: {e}")
        print("Please check your Google Cloud credentials and configuration")

if __name__ == "__main__":  # Entry point when script is run directly
    main()  # Execute main function