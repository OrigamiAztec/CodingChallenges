#Antonio Diaz, TAMU, antonio.diaz.hsa@tamu.edu, Dec 16, 2019
#Using linear regression for stock prediction
#Ctrl alt N to run code in Visual Studio Code


#importing packages to update and graph stock prices
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web

import pandas_datareader as pdr
import datetime
import time
import pandas
import matplotlib.pyplot as plt
import csv
from matplotlib import style
from pandas.plotting import register_matplotlib_converters

register_matplotlib_converters()
start_date = datetime.datetime(2017, 1, 1)
end_date = datetime.datetime(2019, 8, 29)
# Testing import file by outputting Apple stock values, I think
start_time = time.time()
apple_stock = pdr.get_data_yahoo('AAPL', start_date, end_date)

apple_stock.to_csv('aapl_ohlc.csv')
df = pandas.read_csv('aapl_ohlc.csv', header=0, index_col='Date', parse_dates=True)

export_excel = df.to_excel(r'export_dataframe.xlsx', index=None, header=True) #Don't forget to add '.xlsx' at the end of the path

date = []
highs = []

# reading csv file
with open('aapl_ohlc.csv', 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    #
    for row in csvreader:
        date.append(row[0])
        highs.append(row[1])

style.use('ggplot')

# Plot the closing prices for `aapl`
#apple_stock['Close'].plot(grid=True)
df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
print(df['100ma'])

# outputting closing values on y axis
#df['Adj Close'].plot()

ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=1, colspan=1, sharex = ax1)
plt.title("AAPL Stock")
ax1.plot(df.index, df['100ma'])
ax1.plot(df.index, df['Adj Close'])
ax2.bar(df.index, df['Volume'])


# Show the plot
plt.show()

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(1347517370)))

import datetime
from pytz import timezone
import pytz

date_str = '2017-01-03'
# str_to_dt is `naive`
str_to_dt = datetime.datetime.strptime(date_str, '%Y-%m-%d')
print("Str to dt")
print(str_to_dt)                      # 2018-04-01 2056
print(str_to_dt.timestamp())          # 1522581056.0
