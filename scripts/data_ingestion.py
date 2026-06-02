import pandas as pd
import os

data_path = "data/raw"

files = os.listdir(data_path)

for file in files:
    if file.endswith(".xlsx"):
        print("\n" + "="*60)
        print("FILE:", file)

        df = pd.read_excel(os.path.join(data_path, file))

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())