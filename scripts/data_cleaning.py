import pandas as pd

df = pd.read_csv("data/raw/07_scheme_performance.csv")

# Convert return columns to numeric
return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct"
]

for col in return_cols:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# Remove rows with missing returns
df = df.dropna(subset=return_cols)

# Expense ratio validation
df = df[
    (df["expense_ratio_pct"] >= 0.1) &
    (df["expense_ratio_pct"] <= 2.5)
]

# Flag anomalies
anomalies = df[
    (df["return_1yr_pct"] > 100) |
    (df["return_1yr_pct"] < -100)
]

print("Anomalies Found:")
print(len(anomalies))

# Save cleaned file
df.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("Rows:", len(df))
print("Scheme Performance Cleaned Successfully!")