from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import urllib.request
import pandas as pd
import requests
from bs4 import BeautifulSoup
import os
import time

def scrape_images_from(url):
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Create a BeautifulSoup object
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Find all <img> tags in the HTML
    img_tags = soup.find_all('img')
    
    # Create a directory to store the images
    if not os.path.exists('scraped_images'):
        os.makedirs('scraped_images')
    
    # Download and save the images
    image_name=[]
    image_url=[]
    for img in img_tags:
        img_url = img['src']
        img_name = img['src'].split('/')[-1]  # Extract the image file name
        img_path = os.path.join('scraped_images', img_name)
        try:
            # Send a GET request to download the image
            img_data = requests.get(img_url).content
            #print(img_url)
            # Save the image to the specified path
            if img_name.endswith('.svg'):
            	pass
            else:
            	with open(img_path, 'wb') as f:
            		f.write(img_data)
            		image_name.append(img_name)
            		image_url.append(img_url)
            		print(f"Image '{img_name}' downloaded successfully!")
        except:
            print(f"Failed to download image '{img_name}'.")
    data = {'URL': image_url, 'Name': image_name}
    df = pd.DataFrame(data)     
    #print(df)
    df.to_excel('Links_name.xlsx', index=False)

def scrape_images(url):
    

    # Configure Selenium to use Chrome WebDriver
    driver = webdriver.Chrome()

    # Load the webpage
    driver.get(url)

    # Wait for the page to load completely (adjust the sleep duration if needed)
    time.sleep(5)

    # Extract image URLs using JavaScript for images with the specified class
    img_urls = driver.execute_script(
        """
        var imgElements = document.getElementsByClassName('pdp-thumb w-11/12 box-border border border-slate-300 m-4 rounded-lg');
        var imgUrls = [];
        for (var i = 0; i < imgElements.length; i++) {
            var img = imgElements[i];
            imgUrls.push(img.src);
        }
        return imgUrls;
        """
    )

    # Download the images
    counter = 0
    url_list = []
    image_name = []
    svg_img = 0
    for image_url in img_urls:
        print(image_url)
        try:
            name_of_image = image_url.split("/")[-1]
            
            if name_of_image.endswith('.png') or name_of_image.endswith('.jpg'):
                
                urllib.request.urlretrieve(image_url, name_of_image)
                image_name.append(name_of_image)
                url_list.append(image_url)
        except:
            pass

    # Store the image URLs and names in a DataFrame and save as Excel
    if len(image_name) > 1:
        data = {'URL': url_list, 'Name': image_name}
        df = pd.DataFrame(data)
        df.to_excel('output.xlsx', index=False)
    else:
        scrape_images_from(url)

    # Close the browser
    driver.quit()

if __name__ == "__main__":
    scrape_images('https://www.online4baby.com/ickle-bubba-rotator-360-spin-group-0123-car-seat-black')

