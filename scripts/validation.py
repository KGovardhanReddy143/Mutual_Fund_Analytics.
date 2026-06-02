import pandas as pd
import os

files = [
    "data/raw/hdfc_top100_nav.csv",
    "data/raw/sbi_bluechip_nav.csv",
    "data/raw/icici_bluechip_nav.csv",
    "data/raw/axis_bluechip_nav.csv",
    "data/raw/kotak_bluechip_nav.csv",
    "data/raw/nippon_largecap_nav.csv"
]

for file in files:
    df = pd.read_csv(file)
    print("\nFile:", os.path.basename(file))
    print("Columns:", df.columns.tolist())
    print("Rows:", len(df))