import pandas as pd

data = {'Stock': ['AAPL', 'GOOGL'], 'Price': [150, 2800]}
df = pd.DataFrame(data)
print(df)
#    Stock  Price
# 0   AAPL    150
# 1  GOOGL   2800

#How do you read a CSV file?
# Read CSV with UTF-8-sig to handle BOM (Excel files)
df = pd.read_csv('stocks.csv', encoding='utf-8-sig')

# Print first rows to check
print(df.head())

# Print exact column names
print("Columns:", df.columns.tolist())

# Strip extra spaces
df.columns = df.columns.str.strip()

#How do you filter data?
# high_price = df[df['Price'] > 500]
# print(high_price)
