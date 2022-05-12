from vptrade.indicators.oscillators import Oscillator
import pandas as pd

data = pd.read_csv(r'C:\Users\forst\Downloads\TSLA.csv',
                   index_col='Date',
                   parse_dates=True)
oscillator = Oscillator(data)
bollinger = oscillator.rsi(period=14, volume="Close", show="single")