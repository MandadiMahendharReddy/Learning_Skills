# Reading/Writing Text Files:
# Write
from operator import index

with open('example.txt', 'w') as f:
    f.write('Hello World')
# Read
with open('example.txt', 'r') as f:
    content = f.read()
print('example.txt:', content)

# Reading/Writing CSV:
import csv
# Write
with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(['Alice', 22])
# Read
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Reading/Writing JSON:
import json
# Write
with open('data.json', 'w') as f:
    json.dump({'name': 'Bob', 'age': 30}, f)
# Read
with open('data.json', 'r') as f:
    data = json.load(f)
print(data)

# Append to file
with open('example.txt', 'a') as f:
    f.write('New log line\n')

# Open file for read and write
# with open('file.txt', 'r+') as f: # file.txt must exist, error getting
#     content = f.read()
#     f.write('\nExtra line')

# Open file in w+ mode: write and then read
with open('example_wplus.txt', 'w+') as f:
    # Write content to file
    f.write("Hello Mahendhar!\nWelcome to file handling in Python.")

    # Move the cursor back to the start of the file
    f.seek(0)

    # Now read the content
    content = f.read()
    print("File Content:\n", content)

print("============================challenge==============================")

# 🔹 1. 'r' – Read Mode Challenge
# Read an existing file called 'bio.txt' and print all the lines in uppercase.
# If the file doesn’t exist, show a friendly message.

# 🔹 2. 'w' – Write Mode Challenge
# Write your name, age, and favorite language to a file called 'profile.txt'.
# Existing content should be overwritten.

# 🔹 3. 'a' – Append Mode Challenge
# Add the current timestamp (using datetime.now()) to 'log.txt' each time the program runs.
# The log file should retain all previous entries.

# 🔹 4. 'r+' – Read and Write Mode Challenge
# Open 'score.txt' which contains a number (e.g., 150).
# Read the score, add 10 points, and overwrite the updated score at the top.
# If file is missing, show an error.

# 🔹 5. 'w+' – Write and Read Mode Challenge
# Create a new file 'note.txt', write a message, then read and print it.
# Use seek(0) after writing to read the file content.

# 🔹 6. 'a+' – Append and Read Mode Challenge
# Open 'comments.txt' in append mode and let the user enter a comment.
# After writing, read all comments and display them.
# Use seek(0) before reading.

# 🔹 7. 'x' – Exclusive Creation Challenge
# Try to create a file 'first_time.txt'.
# If it already exists, display "File already exists, not created again."

# 🔹 8. 'b' – Binary Mode Challenge
# Open an image file 'photo.jpg' in binary read mode, then copy it to 'copy_photo.jpg'.
# Use 'rb' and 'wb' for this task.

# 🔹 9. 't' – Text Mode Challenge (default)
# Open any text file in 'rt' mode and print the number of lines.
# Bonus: Count how many lines contain the word "Python".

# 💡 Bonus Challenge – Combine Modes
# Open 'userdata.txt' in 'a+' mode.
# Append a new name.
# Then read and display all the user names from the file.
# 1. 'r' – Read Mode Challenge
try:
    with open('bio.txt', "r") as f:
        content = f.read()
    content = content.upper()
except:
    content = "File not found please create and try"
print(content)

#2. 'w' – Write Mode Challenge
import csv
with open("profile.txt", "w") as f:
    writer = csv.writer(f)
    writer.writerow(['Name','Age', 'Favorite Language'])
    writer.writerow(['Advait', '3', 'Mathematics'])
    writer.writerow(['Mahendhar', '32', 'EVS'])

# 3. 'a' – Append Mode Challenge
from datetime import datetime
with open('log.txt', 'a') as f:
    f.write(datetime.now().strftime("%d-%b-%Y (%H:%M:%S.%f)")+ '\n')

# 4. 'r+' – Read and Write Mode Challenge
try:
    with open('score.txt', "r+") as f:
        score=f.read()
        score=int(score)
        score=score+10
        f.seek(0)         # Moves the file pointer to the beginning for writing.
        f.write(str(score))
        f.truncate()     # Removes the remaining old content after the new score.
except:
    score = "File not found please create and try"
print(score)

# 5. 'w+' – Write and Read Mode Challenge

with open('note.txt', "w+") as f:
    f.write("my self mahendhar, i am practicing file handling")
    f.seek(0)
    content=f.read()
    print(content)

# 6. 'a+' – Append and Read Mode Challenge

with open('comments.txt', "a+") as f:
    # Ask the user to enter a comment
    comment = input("Enter your comment: ")
    # Write the new comment to the file
    f.write(comment + '\n')
    f.seek(0)
    content = f.read()
    print(content)

# 7. 'x' – Exclusive Creation Challenge
try:
    with open('first_time.txt', 'x') as f:
        f.write("checking file")
    content = "wrote text in file"
except:
    content= "File already exist, don't create again"
print(content)

# 8. 'b' – Binary Mode Challenge

# Open the source image file in binary read mode ('rb')
with open('passport.jpg', 'rb') as source:
    # Read the entire file contents as bytes into the variable img_data
    img_data = source.read()
    print(img_data)

# Open the destination file in binary write mode ('wb')
with open('copy_passport.jpg', 'wb') as dest:
    # Write the bytes from img_data into the new file (copy_passport.jpg)
    dest.write(img_data)

# 9. 't' – Text Mode Challenge (default)

# Open the file in 'rt' mode (read text mode)
with open('example_wplus.txt', 'rt') as file: # 'rt' mode is the default for open(), so open('example.txt') is equivalent.
    lines = file.readlines()  # Read all lines into a list
num_lines = len(lines)  # Total number of lines
python_count = sum(1 for line in lines if 'Python' in line)  # Lines containing 'Python'

print("Total number of lines:", num_lines)
print("Number of lines containing 'Python':", python_count)

# 💡 Bonus Challenge – Combine Modes
# Open 'userdata.txt' in 'a+' mode.
# Append a new name.
# Then read and display all the user names from the file.
# Open 'userdata.txt' in 'a+' mode (append and read)
with open('userdata.txt', 'a+') as file:
    # Append a new user name at the end of the file
    file.write('NewUser\n')

    # Move the file pointer to the beginning to read all contents
    file.seek(0)

    # Read all lines (user names)
    users = file.readlines()

    # Display all user names
    print("User names in the file:")
    for user in users:
        print(user.strip())