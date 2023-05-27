import requests
from bs4 import BeautifulSoup
import os

def scrape_images(url):
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
    for img in img_tags:
        img_url = img['src']
        img_name = img['src'].split('/')[-1]  # Extract the image file name
        img_path = os.path.join('scraped_images', img_name)
        
        try:
            # Send a GET request to download the image
            img_data = requests.get(img_url).content
            #print(img_url)
            # Save the image to the specified path
            with open(img_path, 'wb') as f:
            	f.write(img_data)
            
            print(f"Image '{img_name}' downloaded successfully!")
        except:
            print(f"Failed to download image '{img_name}'.")

# Example usage
scrape_images('https://www.tradebase.com/fairford-kingsly-600mm-white-floor-standing-cabinet-w-basin/')

