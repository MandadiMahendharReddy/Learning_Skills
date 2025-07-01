import re

email = "user@example.com"
pattern = r"\b[\w.-]+@[\w.-]+\.\w{2,4}\b"

if re.match(pattern, email):
    print("Valid email")
else:
    print("Invalid email")

# 1. re.match()
import re
print(re.match(r"\d+", "123abc"))  # Matches
print(re.match(r"\d+", "abc123"))  # None
# 2. re.search()
print(re.search(r"\d+", "abc123xyz"))  # Match: 123
# 3. re.findall(): Returns all non-overlapping matches as a list.
print(re.findall(r"\d+", "abc123xyz456"))  # ['123', '456']
# 4. re.sub(): Replaces the matched pattern with something else.
print(re.sub(r"\d+", "###", "ID123 and Code456"))  # ID### and Code###
# 5. re.split(): Splits string at each match of the pattern.
print(re.split(r"[,;]", "apple,banana,grapes"))  # ['apple', 'banana', 'grapes']
# 6. re.compile(): Compiles a regex pattern into a regex object for reuse.
pattern = re.compile(r"\d+")
print(pattern.findall("Room1 and Room2"))  # ['1', '2']

# Real-Time Use Case Example: Validate Email Address
import re
email = "user@example.com"
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
if re.match(pattern, email):
    print("Valid email address")
else:
    print("Invalid email address")

print("=================================Regex Patterns========================================")

# ✅ Types of Regex Patterns with Examples (Python)

# . (Dot) - Matches any character except newline
# Example:
import re
print(re.search(r"h.t", "hat"))  # Match

# ^ (Caret) - Matches the start of a string
print(re.match(r"^Hello", "Hello World"))  # Match

# $ (Dollar) - Matches the end of a string
print(re.search(r"end$", "this is the end"))  # Match

# * (Asterisk) - Matches 0 or more repetitions
print(re.findall(r"ab*", "abbb"))  # ['abbb']

# + (Plus) - Matches 1 or more repetitions
print(re.findall(r"ab+", "abbb"))  # ['abbb']

# ? (Question Mark) - Matches 0 or 1 occurrence
print(re.match(r"ab?", "ab"))  # Match

# {n} - Matches exactly n repetitions
print(re.search(r"\d{3}", "Phone: 123-456"))  # Match '123'

# {n,} - Matches n or more repetitions
print(re.findall(r"\d{2,}", "ab1234"))  # ['1234']

# {n,m} - Matches between n and m repetitions
print(re.findall(r"\d{2,4}", "ab12345"))  # ['1234']

# [] (Character Set) - Matches any one character inside brackets
print(re.findall(r"[aeiou]", "hello"))  # ['e', 'o']

# [^] (Negated Set) - Matches any character NOT in brackets
print(re.findall(r"[^0-9]", "a1b2"))  # ['a', 'b']

# \d - Matches any digit (0-9)
print(re.search(r"\d", "age 256"))  # Match '2'

# \D - Matches any non-digit
print(re.findall(r"\D", "123abc"))  # ['a', 'b', 'c']

# \w - Matches any word character (letters, digits, underscore)
print(re.findall(r"\w", "var_1"))  # ['v', 'a', 'r', '_', '1']

# \W - Matches any non-word character
print(re.findall(r"\W", "hello!"))  # ['!']

# \s - Matches whitespace (space, tab, newline)
print(re.findall(r"\s", "hi there"))  # [' ']

# \S - Matches non-whitespace
print(re.findall(r"\S", "a b"))  # ['a', 'b']

# | (Pipe OR) - Matches either pattern
print(re.search(r"cat|dog", "I like dog"))  # Match 'dog'

# () - Grouping expressions
print(re.findall(r"(ab)+", "ababab"))  # ['ab']

# a real-time Python example that simulates a form validation system using all major regex patterns in one program. It includes checks for:
# Username
# Email
# Phone number
# Password strength
# Age
# Address
# All using different regex patterns.

import re

def validate_form(data):
    print("\nForm Validation Results:\n")

    # 1. Username: Must start with a letter, contain only letters/numbers/underscore, 3-15 chars
    if re.fullmatch(r"^[a-zA-Z][a-zA-Z0-9_]{2,14}$", data["username"]):
        print("Username is valid.")
    else:
        print("Invalid username. Use 3-15 letters, numbers or underscores, starting with a letter.")

    # 2. Email: basic email pattern
    if re.fullmatch(r"^[\w\.-]+@[\w\.-]+\.\w{2,4}$", data["email"]):
        print("Email is valid.")
    else:
        print("Invalid email format.")

    # 3. Phone Number: Exactly 10 digits, optional +91 prefix
    if re.fullmatch(r"^(\+91)?\d{10}$", data["phone"]):
        print("Phone number is valid.")
    else:
        print("Invalid phone number. Must be 10 digits or start with +91.")

    # 4. Password: Minimum 8 chars, at least 1 uppercase, 1 lowercase, 1 number, 1 special char
    if re.fullmatch(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$", data["password"]):
        print("Password is strong.")
    else:
        print("Password must have uppercase, lowercase, number, special char and 8+ length.")

    # 5. Age: Only digits, and must be 1 or 2 digits
    if re.fullmatch(r"^\d{1,2}$", data["age"]):
        print("Age is valid.")
    else:
        print("Invalid age.")

    # 6. Address: Should not contain special symbols like @, #, $, %, etc.
    if re.fullmatch(r"^[a-zA-Z0-9\s,.-]+$", data["address"]):
        print("Address is valid.")
    else:
        print("Invalid characters in address.")

# 🧪 Sample form data
form_data = {
    "username": "Mahendhar_25",
    "email": "mahendhar@example.com",
    "phone": "+919999998888",
    "password": "Python@123",
    "age": "25",
    "address": "H.No. 5-9, Main Street, Hyderabad"
}

validate_form(form_data)