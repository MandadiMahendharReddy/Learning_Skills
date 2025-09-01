import pandas as pd
import matplotlib.pyplot as plt

# 1. Read CSV (your file is space-separated)
df = pd.read_csv('stocks.csv', sep=r'\s+', engine='python')

# 2. Clean column names
df.columns = df.columns.str.strip().str.replace('\ufeff', '')

# 3. Check data
print(df.head())
print("Columns:", df.columns.tolist())

# 4. Filter rows where Price > 500
high_price = df[df['Price'] > 500]
print("\nHigh Price Stocks:\n", high_price)

# 5. Line Chart (Stock vs Price)
plt.figure(figsize=(6,4))
plt.plot(df['Stock'], df['Price'], marker='o', linestyle='-', color='blue')
plt.title("Stock Prices - Line Chart")
plt.xlabel("Stock")
plt.ylabel("Price")
plt.show()

# 6. Bar Chart
plt.figure(figsize=(6,4))
plt.bar(df['Stock'], df['Price'], color='orange')
plt.title("Stock Prices - Bar Chart")
plt.xlabel("Stock")
plt.ylabel("Price")
plt.show()

# 7. Histogram (distribution of prices)
plt.figure(figsize=(6,4))
plt.hist(df['Price'], bins=5, color='green', edgecolor='black')
plt.title("Stock Price Distribution - Histogram")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

