# Importing libraries
from bs4 import BeautifulSoup
import os
import requests
import pandas as pd



# Initializing list to store image information
image_names, image_dates, image_styles, image_genres = [], [], [], []

#### This portion in some loop ####
# Accessing painting webpage
url = 'https://www.wikiart.org/en/claude-monet/the-garden-of-the-princess-1867'
r_painting_page = requests.get(url)
soup = BeautifulSoup(r_painting_page.text, 'lxml')

# Getting image name
image = soup.find_all('img', {'class': 'ms-zoom-cursor'})[0]
image_url = image['src'].split('!')[0]
name = image_url.split('/')[-1]

# Getting date of creation
date_created = soup.find("span", itemprop="dateCreated").text

# Getting style and genre
info = soup.find_all('li', {'class': 'dictionary-values'})
style = info[0].find('a').text
genre = info[1].find('a').text

# Storing info
image_names.append(name)
image_dates.append(date_created)
image_styles.append(style)
image_genres.append(genre)
##################################

# Creating data frame from image info lists
images_df = pd.DataFrame({'name': image_names, 
                          'date': image_dates, 
                          'style': image_styles, 
                          'genre': image_genres}
                        )