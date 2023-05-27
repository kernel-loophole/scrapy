import requests
import urllib.request

# URL of the image you want to download

# Extract the file name from the URL

# Download the image and save it to a file
urllib.request.urlretrieve(image_url, file_name)

print('Image downloaded successfully.')
from bs4 import BeautifulSoup

# URL of the web page containing the <img> tag
url = 'https://www.online4baby.com/ickle-bubba-rotator-360-spin-group-0123-car-seat-black'

# Send a GET request to the web page
response = requests.get(url)

# Create a BeautifulSoup object with the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all <img> tags on the page
img_tags = soup.find_all('img')

# Iterate over each <img> tag and print the source URL
for img_tag in img_tags:
	image_url = 'https://www.online4baby.com/ickle-bubba-rotator-360-spin-group-0123-car-seat-black'+img_tag['src']
	print(image_url)

# Send a GET request to the image URL
	response = requests.get(image_url)

# Check if the request was successful
	file_name = image_url.split('/')[-1]
    	urllib.request.urlretrieve(image_url, file_name)

	if response.status_code == 200:
    # Extract the file name from the URL


    # Open a file in binary write mode
    		with open(file_name, 'wb') as file:
        # Write the image content to the file
        		file.write(response.content)

    		print('Image downloaded successfully.')
	else:
    		print('Failed to download the image.')
    		src = img_tag['src']
    		print(src)

