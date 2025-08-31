import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# 1. Fetch real-time stock data (last 6 months for Apple)
stock = yf.Ticker("AAPL")
df = stock.history(period="6mo")  # 6 months of data

# 2. Check the data
print(df.head())
print("Columns:", df.columns.tolist())

# 3. Basic Analysis
print("\nSummary Statistics:\n", df.describe())
print("\nHighest Closing Price:", df['Close'].max())
print("Lowest Closing Price:", df['Close'].min())
print("Average Closing Price:", df['Close'].mean())

# 4. Moving Average (20-day & 50-day)
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()

# 5. Line Chart: Closing Price + Moving Averages
plt.figure(figsize=(10,6))
plt.plot(df.index, df['Close'], label='Close Price', color='blue')
plt.plot(df.index, df['MA20'], label='20-Day MA', color='red')
plt.plot(df.index, df['MA50'], label='50-Day MA', color='green')
plt.title("AAPL Stock Price with Moving Averages")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.show()

# 6. Bar Chart: Trading Volume
plt.figure(figsize=(10,6))
plt.bar(df.index, df['Volume'], color='orange')
plt.title("AAPL Trading Volume")
plt.xlabel("Date")
plt.ylabel("Volume")
plt.show()

# 7. Histogram: Distribution of Daily Returns
df['Daily Return'] = df['Close'].pct_change()
plt.figure(figsize=(8,5))
plt.hist(df['Daily Return'].dropna(), bins=30, color='purple', edgecolor='black')
plt.title("Distribution of Daily Returns")
plt.xlabel("Daily Return")
plt.ylabel("Frequency")
plt.show()
