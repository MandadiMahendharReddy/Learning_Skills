# 1. try-except
try:
    x = int("abc")
except ValueError:
    print("Only numeric input allowed.")

# 2. try-except-else Block
try:
    x = int("10")
except ValueError:
    print("Invalid number.")
else:
    print("Conversion successful:", x)

# 3. try-except-finally Block
try:
    file = open("data.txt")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleaning up (e.g., closing file)")

# 4. Handling Multiple Exceptions
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")
except ValueError:
    print("Invalid input!")

# 5.Catching All Exceptions (Not Recommended for All Cases)
try:
    risky_code()
except Exception as e:
    print("An error occurred:", e)

print("===========================Real Time Example===============================")

# Accepts user input (e.g., withdrawal amount),
# Handles invalid data,
# Performs division (for EMI logic),
# Manages files (like transaction logs),
# Cleans up after actions (finally block).


def withdraw_money(balance):
    try:
        # 1. Input amount from user
        amount = int(input("Enter amount to withdraw: "))

        # 2. Validate withdrawal
        if amount <= 0:
            raise ValueError("Amount must be positive!")

        # 3. Check if sufficient balance
        if amount > balance:
            raise Exception("Insufficient funds!")

    except ValueError as ve:
        print("Invalid input:", ve)

    except Exception as e:
        print("Transaction failed:", e)

    else:
        # 4. If everything goes well
        balance -= amount
        print(f"Transaction successful! Remaining balance: ₹{balance}")

        # 5. Write transaction to file
        try:
            with open("transaction_log.txt", "a") as f:
                f.write(f"Withdrawn: ₹{amount}\n")
        except Exception as e:
            print("Could not write to log file:", e)

    finally:
        print("Thank you for banking with us. Visit again!")

# Call function
withdraw_money(balance=5000)


