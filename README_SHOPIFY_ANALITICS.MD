# Shopify Data Integration: PRODUCT_ANALITICS

## Introduction
This Python script integrates and processes Shopify data by interacting with the Shopify GraphQL API, MySQL, and BigQuery. The script retrieves daily product statistics from Shopify, stores them in a MySQL database, and updates a corresponding BigQuery table.

## Functions

### `create_mysql_table`
Creates a MySQL table with the specified schema if it doesn't exist.

### `update_table_schema`
Checks and updates the schema of an existing MySQL table based on the DataFrame columns.

### `insert_data_into_mysql_table`
Inserts data from a DataFrame into a MySQL table.

### `BG_create_table_if_not_exists`
Creates a BigQuery table if it doesn't exist, using the schema derived from the DataFrame columns.

### `BG_check_and_update_table_schema`
Checks and updates the schema of an existing BigQuery table based on the DataFrame columns.

### `BG_insert_data_into_table`
Inserts data from a DataFrame into a BigQuery table.

### `get_data`
Retrieves product statistics from Shopify for a given product ID and date range using the Shopify GraphQL API.

### `process_data`
Processes retrieved data by creating/updating MySQL and BigQuery tables and inserting data.

## Usage
1. Connects to MySQL and retrieves a list of Shopify products.
2. For each product, retrieves daily statistics using the `get_data` function.
3. Processes the data using the `process_data` function, updating MySQL and BigQuery tables.

## Dependencies
- `mysql-connector`: Python connector for MySQL.
- `google-cloud-bigquery`: Google Cloud client library for BigQuery.
- `pandas`: Data manipulation library.
- `requests`: HTTP library for API requests.
- `datetime`: Standard library for handling dates and times.

## Configuration
- MySQL connection details (host, username, password, database) are specified in the script.
- Shopify API credentials (access token) are provided in the script.
- BigQuery dataset ID is hardcoded in the `BG_create_table_if_not_exists` function.

## Conclusion
This script provides an end-to-end solution for fetching Shopify product statistics, storing them in MySQL, and updating a corresponding BigQuery table. It ensures data integrity and consistency across different data storage systems.
