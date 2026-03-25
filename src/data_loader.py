import pandas as pd

def load_data(path="../data/nifty50_raw.csv"):
    data = pd.read_csv(path, index_col=0, parse_dates=True)
    data = data.sort_index()
    return data