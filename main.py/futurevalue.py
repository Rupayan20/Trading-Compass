import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from datetime import date, timedelta

from pandas_datareader import data as pdr
import yfinance as yf
yf.pdr_override()   # override pandas_datareader

# Prompt the user to enter the stock symbol
ticker = input("Enter the stock symbol: ")

start_date = '2000-01-01'
end_date = (date.today()).strftime('%Y-%m-%d')   # get tomorrow's date

data = pdr.get_data_yahoo(ticker, start_date, end_date)

print(data.head())
plt.plot(data['Close'], label='Actual Price')
plt.title(ticker + ' Stock Price')
plt.xlabel('Year')
plt.ylabel('Price ($)')
plt.legend()
plt.show()
print(data.describe())

prediction_days = 35  # predict the next 35 days
data['Prediction'] = data['Close'].shift(-prediction_days)

X = np.array(data.drop(['Prediction'], 1))
X = X[:-prediction_days]
y = np.array(data['Prediction'])
y = y[:-prediction_days]

split = int(0.8 * len(data))
X_train, X_test, y_train, y_test = X[:split], X[split:], y[:split], y[split:]

regressor = LinearRegression()
regressor.fit(X_train, y_train)

accuracy = regressor.score(X_test, y_test)
print("Accuracy:", accuracy)

prediction = regressor.predict(X_test)
plt.plot(prediction, label='Predicted Price')
plt.plot(y_test, label='Test Data')
plt.title(ticker + ' Stock Price Prediction')
plt.xlabel('hours')
plt.ylabel('Price ($)')
plt.legend()
plt.show()
