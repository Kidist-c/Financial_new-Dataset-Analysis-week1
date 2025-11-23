import numpy as np


# Function to add percentage and log returns

def add_returns(df):
    df['Return']=df['Close'].pct_change()
    df['LogReturn']=np.log(df["Close"] / df["Close"].shift(1))
    return df
