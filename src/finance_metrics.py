import numpy as np

def compute_metrics(df):
    prices = df["Close"]
    returns = prices.pct_change().dropna()
    cumulative_return = (prices.iloc[-1] / prices.iloc[0]) - 1
    volatility = returns.std()

    metrics = {
        "average_daily_return": returns.mean(),
        "cumulative_return": cumulative_return,
        "volatility": volatility
    }
    return metrics
