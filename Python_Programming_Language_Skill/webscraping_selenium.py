from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://quotes.toscrape.com/js/")

# Wait until at least one quote is present
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "text"))
)

quotes = driver.find_elements(By.CLASS_NAME, "text")
for quote in quotes:
    print(quote.text)

driver.quit()



