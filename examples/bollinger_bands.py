from vptrade.indicators.trends import Trend
import pandas as pd

data = pd.read_csv(r'C:\Users\forst\Downloads\TSLA.csv',
                   index_col='Date',
                   parse_dates=True)
trend = Trend(data)
bollinger = trend.bollinger_bands(period=30, volume="Close", show="single", save="bolinger_band.png")