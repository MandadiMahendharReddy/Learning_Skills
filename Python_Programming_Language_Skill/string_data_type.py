# 1. upper()
# Converts all characters to uppercase.
name = "krishna"
print(name.upper())  # KRISHNA

# 2. lower()
# Converts all characters to lowercase.
print("HELLO".lower())  # hello

# 3. capitalize()
# Capitalizes the first character only.
text = "python is fun"
print(text.capitalize())  # Python is fun

# 4. title()
# Capitalizes the first letter of every word.
print("learn python fast".title())  # Learn Python Fast

# 5. strip()
# Removes leading and trailing spaces.
msg = "  hello  "
print(msg.strip())  # 'hello'

# 6. replace(old, new)
# Replaces all occurrences of a substring.
print("bad code".replace("bad", "good"))  # good code


#7. split(separator)
# Splits the string into a list by the given separator.
text = "apple,banana,grapes"
print(text.split(","))  # ['apple', 'banana', 'grapes']

# 8. join(iterable)
# Joins elements of a list into a single string.
words = ["Hello", "World"]
print(" ".join(words))  # Hello World

# 9. find(substring)
# Returns the first index of a substring. Returns -1 if not found.
print("python".find("ho"))  # 3
print("python".find("ma"))  # -1

# 10. count(substring)
# Counts how many times a substring appears.
print("banana".count("a"))  # 3

# 11. startswith(prefix) / endswith(suffix)
# Checks if string starts or ends with the given value.
print("Hello".startswith("He"))  # True
print("file.txt".endswith(".txt"))  # True

# 12. isalpha() / isdigit() / isalnum()
# isalpha() → only letters
# isdigit() → only numbers
# isalnum() → letters + numbers
print("abc".isalpha())  # True
print("123".isdigit())  # True
print("abc123".isalnum())  # True

# 13. index(substring)
# Returns the first index of a substring. Returns ValueError if not found.
print("python".index("ho"))  # 3
# print("python".index("ma"))  # ValueError: substring not found

# Given input
# name = "  mahendhar  "
# email = "Mahendhar@Gmail.COM"
# age = "25"
# bio = "i am a python developer. i love ai and web."
# skills = "python, ai, devops, python"
#  Tasks You’d Perform (using string methods):
#  Clean up name with strip() and capitalize it
#  Make email lowercase using lower()
#  Check if email ends with "@gmail.com" using endswith()
#  Validate that age is a number using isdigit()
#  Capitalize the bio properly using capitalize() or title()
#  Split skills using split(",")
#  Remove duplicates by converting to set, then join again
#  Count how many times “python” appears using count()
#  Check if name is alphabet using isalpha()

def data_validate(name, email, age, bio, skills):
    print('Clean Name:', name.capitalize().strip())
    email=email.lower()
    if email.endswith('@gmail.com'):
        print('Email:', email, '(valid Gmail)')
    if age.isdigit():
        print(age, '(valid)')
    print('Formatted Bio:', bio.title())
    Skills1= (skills.split(', '))
    Skills = set(Skills1)
    print('Skills:', ', '.join(Skills) )
    print("'python' mentioned ", Skills1.count('python'), "times in skills." )

name = "  mahendhar  "
email = "Mahendhar@Gmail.COM"
age = "25"
bio = "i am a python developer. i love ai and web."
skills = "python, ai, devops, python"
data_validate(name, email, age, bio, skills)