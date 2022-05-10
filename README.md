
# vptrade
[![MIT License](https://img.shields.io/apm/l/atomic-design-ui.svg?)](https://github.com/tterb/atomic-design-ui/blob/master/LICENSEs)

vptrade is a technical indicators trading tools can be used to all instruments.



## Requirements

- Python 3.9 or higher
## Features

- Trends Indicator 
- Oscillators Indicator



## Installation

Instal this package with pip

```bash
  pip install vptrade
```
    
# Usage/Examples

## Moving Average
```python
from vptrade.indicators.trends import Trend
import pandas as pd


data = pd.read_csv(r'YOUR PATH\TSLA.csv',
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
```

## Bollinger band
```python
from vptrade.indicators.trends import Trend
import pandas as pd

data = pd.read_csv(r'YOUR PATH\TSLA.csv',
                   index_col='Date',
                   parse_dates=True)
trend = Trend(data)
bollinger = trend.bollinger_bands(period=30, volume="Close", show=True, save="bolinger_band.png")
```


## Support

For support, Join my discord https://discord.gg/HZJZAVAZdr


## Contributing

Contributions are always welcome!

See `contributing.md` for ways to get started.

Please adhere to this project's `code of conduct`.

