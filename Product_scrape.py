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
    #chrome_options = Options()
    #chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--no-sandbox')
    #chrome_options.add_argument('--disable-dev-shm-usage')

    #driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver = webdriver.Chrome()
    #driver.get("https://www.online4baby.com/ickle-bubba-rotator-360-spin-group-0123-car-seat-black")

     # Load the webpage
    driver.get(url)
    
    # Wait for the page to load completely (adjust the sleep duration if needed)
#    time.sleep(10)
    
    # Create a directory to store the images
    
    # Extract image URLs using JavaScript
    img_urls = driver.execute_script(
        """
        var imgElements = document.getElementsByTagName('img');
        var imgUrls = [];
        for (var i = 0; i < imgElements.length; i++) {
            var img = imgElements[i];
            imgUrls.push(img.src);
        }
        return imgUrls;
        """
    )
    image_element = driver.find_elements(By.TAG_NAME, 'img')
    counter=0
    url_list=[]
    image_name=[]
    svg_img=0
    for i in image_element:
    	try:
    		image_url = i.get_attribute('src')
    		name_of_image=image_url.split("/")
    		name_of_img=name_of_image[-1]
    	#print(name_of_img)
    		if name_of_img.endswith('.svg'):
    			svg_img+=1
    			pass
    		else: 
    			if name_of_img.startswith("nuna-travel"):
    				urllib.request.urlretrieve(image_url,name_of_img)
    				image_name.append(name_of_img)
    				url_list.append(image_url)
    	except:
    		#print(i.get_attribute('src'))
    		pass
    	#if len(url_list)!=len(image_name):
    	#	break
    #print(len(url_list),len(image_name))
    if len(image_name)>1:
    	data = {'URL': image_url, 'Name': image_name}
    	df = pd.DataFrame(data)     
    #print(df)
    	df.to_excel('output.xlsx', index=False)
#    else:
  #  	print("calling function")
 #   	scrape_images_from(url)
        
    # Close the browser
 #   driver.quit()
# Example usage
if __name__=="__main__":
	scrape_images('https://discountbabyequip.co.uk/products/nuna-triv-and-pipa-next-i-size-car-seat-travel-system-timber')

