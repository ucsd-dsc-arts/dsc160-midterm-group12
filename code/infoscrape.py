# Importing libraries
from bs4 import BeautifulSoup
import os
import requests
import pandas as pd


DATA_DIR = "../data/"
ARTIST_URL = "https://www.wikiart.org/en/claude-monet/all-works/text-list"
PAINTING_URL = 'https://www.wikiart.org{painting_path}'

artist_page = requests.get(ARTIST_URL)
soup = BeautifulSoup(artist_page.text, 'lxml')

painting_paths = []

# retreive all rows in painting-list
for li in soup.find_all('li', {'class': 'painting-list-text-row'}):

    # retrieve all links in the current row
    for link in li.find_all('a'):
        href = link.get('href')
        # store in dictionary
        painting_paths.append(href)



def download_and_save(painting_url):
    r_painting_page = requests.get(painting_url)
    soup = BeautifulSoup(r_painting_page.text, 'lxml')
    # Initializing list to store image information
    

    for img in soup.find_all('img', {'class': 'ms-zoom-cursor'}):
        img_url = img['src']
        img_url = img_url.split('!')[0]
        #name
        filename = img_url.split('/')[-1]
        #date
        date_created = soup.find("span", itemprop="dateCreated").text
        # Getting style and genre
        info = soup.find_all('li', {'class': 'dictionary-values'})
        style = info[0].find('a').text
        genre = info[1].find('a').text
        
        # Storing info
        image_names.append(filename)
        image_dates.append(date_created)
        image_styles.append(style)
        image_genres.append(genre)
    
        
        
        outfile = os.path.join(DATA_DIR, filename)                       
        if not os.path.exists(outfile):                        
            r = requests.get(img_url, outfile)
            with open(outfile, 'wb') as f:
                f.write(r.content)
        else:
            pass
def make_lists(path, painting_paths):
    """make lists to create dataframe"""
    image_names, image_dates, image_styles, image_genres = [], [], [], []

    for path in painting_paths:
        painting_path = PAINTING_URL.format(painting_path=path)
        download_and_save(painting_path)
##################################

# Creating data frame from image info lists
image_df=pd.DataFrame({'name': image_names, 'date': image_dates, 'style': image_styles, 'genre': image_genres})
image_df.drop_duplicates(inplace= True)
image_df.reset_index(inplace=True)
image_df=image_df[["name","date","style", "genre"]]