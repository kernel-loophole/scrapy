from selenium import webdriver
import urllib.request
from selenium.webdriver.common.by import By

# Initialize the Selenium webdriver
driver = webdriver.Chrome()

# Navigate to the webpage containing the image
driver.get('https://www.online4baby.com/ickle-bubba-rotator-360-spin-group-0123-car-seat-black')

# Find the image element
image_element = driver.find_element(By.TAG_NAME, 'img')

# Get the source URL of the image
image_url = image_element.get_attribute('src')

# Download the image
urllib.request.urlretrieve(image_url, 'image.jpg')

# Close the webdriver
driver.quit()

