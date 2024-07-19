# MIS_Project

## Snowflake Setup Guide

### 1. Create a Snowflake Account

1. Visit the [Snowflake signup page](https://signup.snowflake.com).
2. Follow the instructions to create an account.
3. During signup, choose a username that will be useful for programmatic connections.

### 2. Create a Database

1. Log in to the Snowflake web interface.
2. Navigate to **Data** > **Databases**.
3. Click on **+ Database** to create a new database.

### 3. Create a Schema

1. Select the database you just created.
2. Click on **+ Schema** to create a new schema within the selected database.

### 4. Create a Warehouse

1. Click on **Admin** > **Warehouses**.
2. Click on **+ Warehouse** to create a new warehouse.

### 5. Fetch Account Details

1. Click on **Admin** > **Account**.
2. Copy the Account URL (e.g., `https://hello-abc12345.snowflakecomputing.com`).
3. Edit this URL to extract only the details between `https://` and `.snowflakecomputing.com` (e.g., `hello-abc12345`).

### Notes

- Ensure you have appropriate permissions to create databases, schemas, and warehouses.
- The extracted account details are useful for programmatic access and configurations.

For more detailed instructions and advanced configurations, refer to the [Snowflake documentation](https://docs.snowflake.com).
