from vptrade.indicators.trends import Trend
from vptrade.strategies.moving_average import MovingAverageStrategy

trend = Trend(path=r'C:\Users\forst\Downloads\TSLA.csv')
ema_14 = trend.ema(period=20, volume="Close")
ema_100 = trend.ema(period=100, volume="Close")
ema_200 = trend.ema(period=200, volume="Close")

MA = MovingAverageStrategy()
signal = MA.crossover([ema_14, ema_100, ema_200], show="strategy")