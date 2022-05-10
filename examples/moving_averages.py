from vptrade.indicators.trends import Trend
import pandas as pd


data = pd.read_csv(r'C:\Users\forst\Downloads\TSLA.csv',
                   index_col='Date',
                   parse_dates=True)
trend = Trend(data)

#simple moving average
sma = trend.sma(period=30, volume="Close", show=True, save="sma_img.png")

#exponential moving average
ema = trend.ema(period=30, volume="Close", show=True, save="ema_img.png")

#cummulative moving average show only without save
cma = trend.cma(period=30, volume="Close", show=True)

#smoothed moving average without save and show
smma = trend.smma(period=30, volume="Close", show=False)

#lienar-weighted moving average without show and save
lwma = trend.lwma(period=30, volume="Close")
