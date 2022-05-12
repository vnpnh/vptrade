from vptrade.indicators.trends import Trend
import pandas as pd

data = pd.read_csv(r'C:\Users\forst\Downloads\TSLA.csv',
                   # index_col='Date',
                   parse_dates=True)
trend = Trend(data)

# simple moving average
sma = trend.sma(period=30, volume="Close", show="single", save="sma_img.png")

# exponential moving average
ema = trend.ema(period=30, volume="Close",  show="single", save="ema_img.png")

# cummulative moving average show only without save
cma = trend.cma(period=30, volume="Close",  show="single")

# smoothed moving average
smma = trend.smma(period=30, volume="Close",  show="single")

# linear-weighted moving average
lwma = trend.lwma(period=30, volume="Close",  show="single")

