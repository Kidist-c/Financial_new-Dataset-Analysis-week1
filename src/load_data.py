import pandas as pd
# function to load the dataset
def load_data(ticker):
    path=f"../data/{ticker}.csv"
    df=pd.read_csv(path)
    df.dropna(inplace=True)
    return df