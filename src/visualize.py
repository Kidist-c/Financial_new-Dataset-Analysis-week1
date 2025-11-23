import matplotlib.pyplot as plt

def plot_price(df, ticker):
    plt.figure(figsize=(10,5))
    plt.plot(df["Close"])
    plt.title(f"{ticker}: Close Price")
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.show()

def plot_rsi(df, ticker):
    plt.figure(figsize=(10,4))
    plt.plot(df["RSI"])
    plt.axhline(70, linestyle="--")
    plt.axhline(30, linestyle="--")
    plt.title(f"{ticker}: RSI")
    plt.show()

def plot_macd(df, ticker):
    plt.figure(figsize=(10,4))
    plt.plot(df["MACD"], label="MACD")
    plt.plot(df["MACD_signal"], label="Signal")
    plt.legend()
    plt.title(f"{ticker}: MACD")
    plt.show()
