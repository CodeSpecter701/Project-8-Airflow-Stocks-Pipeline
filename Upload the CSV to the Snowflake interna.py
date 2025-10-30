import pandas as pd
import snowflake.connector
from snowflake.connector.pandas_tools import write_pandas

# ✅ 1. Your Snowflake credentials (fill with your details)
USER = "ANOOSH707"
PASSWORD = "your_password"
ACCOUNT = "lrjahvi-yx48243"   # Example: from your Snowflake URL
WAREHOUSE = "COMPUTE_WH"
DATABASE = "STOCKS_DB"
SCHEMA = "AIRFLOW_STOCKS_SCHEMA"

# ✅ 2. Connect to Snowflake
conn = snowflake.connector.connect(
    user=os.getenv("ANOOSH707"),
    password=os.getenv("CloudEngineer101"),
    account=os.getenv("WD65648"),
    warehouse="COMPUTE_WH",
    database="STOCKS_DB",
    schema="AIRFLOW_STOCKS_SCHEMA"
)

# ✅ 3. Read your CSV file
df = pd.read_csv("D:/stocks_data.csv")

# ✅ 4. Create table (optional)
cur = conn.cursor()
cur.execute("""
    CREATE OR REPLACE TABLE STOCKS_PRICES (
        SYMBOL STRING,
        CLOSE FLOAT
    )
""")

# ✅ 5. Upload the data
success, nchunks, nrows, _ = write_pandas(conn, df, "STOCKS_PRICES")
print(f"✅ Loaded {nrows} rows successfully into STOCKS_PRICES table.")

# ✅ 6. Close connection
cur.close()
conn.close()
