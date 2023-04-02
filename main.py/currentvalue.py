# We used "yfinance" library to collect online data, and with it, we can collect the financial data of Yahoo.

import plotly.graph_objects as go
import yfinance as yf

# Get user input for stock ticker symbol
ticker = input('Enter a Stock Name: ')

# Get the stock data from Yahoo Finance
stock = yf.Ticker(ticker)
df = stock.history(period='max')
df = df.reset_index()

# Create the plot
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], mode='lines', name='Price'))

# Add hover text to display values
fig.update_layout(hovermode='x unified')
fig.update_traces(hovertemplate='Date: %{x}<br>Price: %{y}')

# Show the plot
fig.show()
