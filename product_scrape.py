import requests
from bs4 import BeautifulSoup
import urllib.parse
import os
from tqdm import tqdm
import pandas as pd
url_list=[]
image_name=[]
url = "https://discountbabyequip.co.uk/products/nuna-triv-and-pipa-next-i-size-car-seat-travel-system-timber"
parent_class_name = "page-content page-content--product"
image_class_name = "image-class"

# Path to store the downloaded images
download_path = "images/"

# Create the download directory if it doesn't exist
os.makedirs(download_path, exist_ok=True)

# Send a GET request to the website
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")

# Find all the parent elements with the specified class name
parent_elements = soup.find_all(class_=parent_class_name)
print("downloading please wait...")
for parent_element in parent_elements:
    image_tags = parent_element.find_all("img")
    for image in tqdm(image_tags):
        try:
            src = 'https:' + image["data-src"]
            urllib.request.urlretrieve(src)
            filename = os.path.join(download_path, os.path.basename(urllib.parse.urlparse(src).path))
            image_response = requests.get(src)
            image_name.append(src)
            url_list.append(src)
            # image_name.append(src)
            # url_list.append(src)
            with open(filename, "wb") as f:
                f.write(image_response.content)

        except:
            pass
data = {'URL': url_list, 'Name': image_name}
df = pd.DataFrame(data)
    #print(df)
df.to_excel('output.xlsx', index=False)
print("All images downloaded successfully!")
