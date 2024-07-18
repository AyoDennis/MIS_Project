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
    CREATE OR REPLACE STAGE s3_stage
    URL = 's3://name-of-s3-bucket/'
    CREDENTIALS = (
      AWS_KEY_ID = 'paste-from-your-credential',
      AWS_SECRET_KEY = 'paste-from-your-credential'
    )
    """
cur.execute(sql_create_stage)
print("External stage created successfully.")