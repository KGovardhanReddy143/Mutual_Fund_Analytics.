import pandas as pd

df = pd.read_csv("data/processed/07_scheme_performance_clean.csv")

risk = input("Enter Risk Appetite (Low/Moderate/High): ")

filtered = df[df["risk_grade"].str.lower() == risk.lower()]

top3 = filtered.sort_values(
    "return_5yr_pct",
    ascending=False
).head(3)

print("\nTop 3 Recommended Funds\n")

print(
    top3[
        [
            "scheme_name",
            "risk_grade",
            "return_5yr_pct",
            "expense_ratio_pct"
        ]
    ]
)