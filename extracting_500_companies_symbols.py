import requests
import pandas as pd
from bs4 import BeautifulSoup
from io import StringIO

WIKI_URL = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"

def fetch_symbols(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )
    }

    resp = requests.get(url, headers=headers)
    resp.raise_for_status()

    soup = BeautifulSoup(resp.text, "html.parser")
    table = soup.find("table", {"id": "constituents"})

    # Fix FutureWarning by wrapping table HTML in StringIO
    df = pd.read_html(StringIO(str(table)))[0]
    return df["Symbol"].tolist()

def main():
    symbols = fetch_symbols(WIKI_URL)
    print(f"✅ Extracted {len(symbols)} symbols.")
    print(symbols[:10])  # show first 10 symbols
    pd.DataFrame(symbols, columns=["Symbol"]).to_csv("sp500_symbols.csv", index=False)
    print("💾 Saved to sp500_symbols.csv")

if __name__ == "__main__":
    main()


# viewing the scrap data of the symbols

def main():
    symbols = fetch_symbols(WIKI_URL)
    print(f"Fetched {len(symbols)} symbols.")
    
    # show first 10 as sample
    print("Sample symbols:", symbols[:10])
    
    write_symbols(symbols, filename="symbols.txt")
    print("Symbols written to symbols.txt")
