import pandas as pd
from sqlalchemy import create_engine

# Create SQLite database
engine = create_engine("sqlite:///./bluestock_mf.db", echo=False)

# Load cleaned files
nav = pd.read_csv("data/processed/02_nav_history_clean.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions_clean.csv")
performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

# Load into SQLite
nav.to_sql("fact_nav", engine, if_exists="replace", index=False)
transactions.to_sql("fact_transactions", engine, if_exists="replace", index=False)
performance.to_sql("fact_performance", engine, if_exists="replace", index=False)

print("NAV Rows:", len(nav))
print("Transaction Rows:", len(transactions))
print("Performance Rows:", len(performance))

print("SQLite Database Loaded Successfully!")