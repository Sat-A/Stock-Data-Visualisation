import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Set the start and end date
start_date = '1990-01-01'
end_date = '2024-08-1'

# Define the ticker list
tickers_list = ['AAPL', 'IBM', 'MSFT', 'WMT']

# Create placeholder for data
data = pd.DataFrame(columns=tickers_list)

# Fetch the data
for ticker in tickers_list:
    data[ticker] = yf.download(ticker,
                               start_date,
                               end_date, auto_adjust=False)['Adj Close']

data.plot(figsize=(10, 7))

# Add labels and title
plt.xlabel('Year')
plt.ylabel('Price')
plt.title('Adjusted close price of stocks')

# Show the plot
plt.show()