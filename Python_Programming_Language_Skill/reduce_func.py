from functools import reduce
numbers = [1, 2, 3, 4, 5]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 15

# Example
from functools import reduce

# Step 1: List of item prices in the shopping cart
cart_prices = [299.99, 499.50, 149.75, 89.90, 250.00]

# Step 2: Use reduce() to calculate the total price
total = reduce(lambda x, y: x + y, cart_prices)

# Step 3: Add 18% GST
gst = total * 0.18
final_amount = round(total + gst, 2)

# Output the results
print("Subtotal (before GST): ₹", round(total, 2))
print("GST (18%): ₹", round(gst, 2))
print("Final Amount to Pay: ₹", final_amount)