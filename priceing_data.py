import yfinance as yf
import pandas as pd

# Load symbols from your previously saved file
import pandas as pd
symbols = pd.read_csv("sp500_symbols.csv")["Symbol"].tolist()


print(f"Loaded {len(symbols)} symbols")

# For testing, you can limit to first 10
# symbols = symbols[:10]

# Download live pricing data
data = yf.download(symbols, period="1d", group_by='ticker', threads=True)

# Flatten data for easy viewing
prices = []
for sym in symbols:
    if sym in data.columns.levels[0]:  # ensure symbol is valid
        close_price = data[sym]['Close'].iloc[-1]
        prices.append({"Symbol": sym, "Close": close_price})

df = pd.DataFrame(prices)
df.to_csv("sp500_prices.csv", index=False)
print(df.head())
print("\nSaved latest prices to sp500_prices.csv")



import os
print("📂 Current working directory:", os.getcwd())



output_path = r"d:\Project 8 Airflow Stocks Pipeline\sp500_prices.csv"
df.to_csv(output_path, index=False)
print(f"✅ Saved to: {output_path}")


