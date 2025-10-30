import pandas as pd

# Read your CSV file
df = pd.read_csv(r"D:\sp500_prices.csv")

# Generate SQL INSERT statements
sql_lines = []
for _, row in df.iterrows():
    symbol = str(row['Symbol']).strip()
    close = row['Close']
    sql_lines.append(f"('{symbol}', {close})")

# Combine into one SQL statement
sql_query = "INSERT INTO STOCKS_PRICES (SYMBOL, CLOSE) VALUES\n" + ",\n".join(sql_lines) + ";"

# Save to .sql file
with open("insert_sp500_prices.sql", "w", encoding="utf-8") as f:
    f.write(sql_query)

print("✅ SQL file 'insert_sp500_prices.sql' created successfully.")
