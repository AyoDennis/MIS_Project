import snowflake.connector
from snowflake.connector import DictCursor

# Snowflake connection parameters
snowflake_user = 'your_snowflake_user'
snowflake_password = 'your_snowflake_password'
snowflake_account = 'your_snowflake_account'
snowflake_warehouse = 'your_snowflake_warehouse'
snowflake_database = 'your_snowflake_database'
snowflake_schema = 'your_snowflake_schema'

# Connection
conn = snowflake.connector.connect(
    user=snowflake_user,
    password=snowflake_password,
    account=snowflake_account,
    warehouse=snowflake_warehouse,
    database=snowflake_database,
    schema=snowflake_schema
)


# Create a cursor object using DictCursor for easier dictionary handling
cur = conn.cursor(DictCursor)


# Create an external stage pointing to your S3 bucket
sql_create_stage = """
    CREATE OR REPLACE STAGE stage_name
    URL = 's3://name_of_s3_bucket/'
    CREDENTIALS = (
      AWS_KEY_ID = 'paste_from_your_credential',
      AWS_SECRET_KEY = 'paste_from_your_credential'
    )
    """
cur.execute(sql_create_stage)
print("External stage created successfully.")


# Create a file format for CSV files
sql_create_file_format = """
    CREATE OR REPLACE FILE FORMAT file_format
    TYPE = 'TYPE_OF_FILE(e.g CSV)'
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    SKIP_HEADER = 1
    FIELD_DELIMITER = ','
    """
cur.execute(sql_create_file_format)
print("File format created successfully.")


# Create a table with a flexible schema
sql_create_table = """
    CREATE OR REPLACE TABLE table_name
    (
        VARIANT_COLUMN VARIANT
    );
    """
cur.execute(sql_create_table)
print("Table with flexible schema created successfully.")

# Test manual data loading from S3 to Snowflake table
sql_copy_into = """
    COPY INTO table_table
    FROM @s3_stage/s3_folder_name/file_name.csv
    FILE_FORMAT = (FORMAT_NAME = 'csv_format')
    ON_ERROR = 'CONTINUE';
    """
cur.execute(sql_copy_into)
print("Data manually loaded successfully.")

# Create a Snowpipe to automatically ingest data into the table
sql_create_pipe = """
CREATE OR REPLACE PIPE NAME_OF_YOUR-PIPE
AUTO_INGEST = TRUE
AS
COPY INTO YOUR_DATABASE_NAME.SCHEMA_NAME.table_name
FROM @stage_name/s3_folder/s3_file.format
FILE_FORMAT = (FORMAT_NAME = 'csv_format')
ON_ERROR = 'CONTINUE';
"""

