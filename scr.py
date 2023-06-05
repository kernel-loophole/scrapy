import requests
from bs4 import BeautifulSoup
import urllib.parse
import os

# URL of the website
url = "https://discountbabyequip.co.uk/products/nuna-triv-and-pipa-next-i-size-car-seat-travel-system-timber"

# Class name of the images you want to download
class_name = "page-content page-content--product"

# Path to store the downloaded images
download_path = "images/"

# Create the download directory if it doesn't exist
os.makedirs(download_path, exist_ok=True)

# Send a GET request to the website
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the image tags with the specified class name
images = soup.find_all(class_=class_name)
#print(images)
# Download each image
for image in images:
    # Get the image source URL
    src = image["src"]

    # Create a filename by extracting the image name from the URL
    filename = os.path.join(download_path, os.path.basename(urllib.parse.urlparse(src).path))

    # Send a GET request to download the image
    image_response = requests.get(src)

    # Save the image to the specified directory
    with open(filename, "wb") as f:
        f.write(image_response.content)

    print(f"Downloaded {filename}")

print("All images downloaded successfully!")

