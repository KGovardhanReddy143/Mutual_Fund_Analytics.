import requests
import pandas as pd

schemes = {
    "sbi_bluechip": "119551",
    "icici_bluechip": "120503",
    "nippon_largecap": "118632",
    "axis_bluechip": "119092",
    "kotak_bluechip": "120841"
}

for name, code in schemes.items():

    url = f"https://api.mfapi.in/mf/{code}"

    response = requests.get(url)

    data = response.json()

    print("\n", data["meta"]["scheme_name"])

    nav_df = pd.DataFrame(data["data"])

    nav_df.to_csv(
        f"data/raw/{name}_nav.csv",
        index=False
    )

    print(f"{name}_nav.csv saved")