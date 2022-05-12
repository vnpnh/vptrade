from vptrade.indicators.trends import Trend
import pandas as pd
from vptrade.plots.visualize import show

data = pd.read_csv(r'C:\Users\forst\Downloads\TSLA.csv',
                   # index_col='Date',
                   parse_dates=True)
trend = Trend(data)


ema_14 = trend.ema(period=14, volume="Close", show="combine")
ema_100 = trend.ema(period=100, volume="Close", show="combine")
show()