
# Date: 4/2/23
# Output: chart the users stock of choice
# currently on 1yr period with intervals of 1d, 
# if you want to change the times must be done manually in the code


import yfinance as yf
import finplot as fplt


# ask user for stock ticker they wanna get info on / see 1yr chart
tick = yf.Ticker(input("Ticker?  "))

# RETRIEVE 1 YEAR WORTH OF DAILY DATA OF TICKER
df = tick.history(interval='1d',period='1y')

# PLOT THE OHLC CANDLE CHART
fplt.candlestick_ochl(df[['Open','Close','High','Low']])
fplt.show()
