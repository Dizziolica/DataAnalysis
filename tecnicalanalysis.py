import pandas_ta as ta
import yfinance as yf
import pandas


df = pandas.DataFrame()
df = df.ta.ticker('AAPL', period='5y')
df.ta.log_return(cumulative=True, append=True)
print(df)
df.ta.indicators()
ind_list = df.ta.indicators()
print(ind_list)

# Create your own Custom Strategy
CustomStrategy = ta.Strategy(
    name="Momo and Volatility",
    description="SMA 50,200, BBANDS, RSI, MACD and Volume SMA 20",
    ta=[
        {"kind": "sma", "length": 50},
        {"kind": "sma", "length": 200},
        {"kind": "bbands", "length": 20},
        {"kind": "rsi"},
        {"kind": "macd", "fast": 8, "slow": 21},
        {"kind": "sma", "close": "volume", "length": 20, "prefix": "VOLUME"},
        ]
        )
# To run your "Custom Strategy"
df.ta.strategy(CustomStrategy)
