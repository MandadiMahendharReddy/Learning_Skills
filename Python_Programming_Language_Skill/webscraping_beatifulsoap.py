import requests

# URL of the webpage you want to download
url = "https://quotes.toscrape.com/js/"

# Send GET request to the website
response = requests.get(url)

# Save the HTML content to a file
with open("downloaded_page1.html", "w", encoding='utf-8') as file:
    file.write(response.text)

print("Page downloaded successfully!")

# Beautiful soup
import requests
from bs4 import BeautifulSoup
url = "https://quotes.toscrape.com/"
response = requests.get(url)
print('response', response)
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all('span', class_='text')
print(type(quotes))
for quote in quotes:
    print(quote.text)

# Advanced BeautifulSoup Use:
# Find by attribute
soup.find_all('input', {'type': 'text'})
# Find by regex
import re
quote1=soup.find_all('a', href=re.compile(r'^https'))
for quote in quote1:
     print(quote.text)
