"""
  Overview

What is done:
    1. Importing
        1. beautiful-soup for accessing web
        2. Request for getting the json and images
        3. os for saving the images in a certain location
    

"""

# @ Imports
from bs4 import *
import requests as rq
import os
from Similar_String import Common_Strings


# * Defining
url = 'https://schools.aglasem.com/23036'

def ExtractPanels(url, images_folder_path):
    """
    """
    r2 = rq.get(url)
    soup2 = BeautifulSoup(r2.text, "html.parser")

    links = []
    
    x = soup2.select(f'img[src^={CommonInLink(url)}]' if CommonInLink(url) else 'img[src]')

    for img in x:
        links.append(img['src'])


    os.chdir(images_folder_path)

    for index, img_link in enumerate(links, 1):
        try:
            img_data = rq.get(img_link).content

            with open(f'{index}.jpg', 'wb+') as f:
                print(f'panel_{index}.jpg sucessfully made! > Extractor')
                f.write(img_data)
        except:
            pass

def CommonInLink(url):
    """
    """
    pass
    r2 = rq.get(url)
    soup2 = BeautifulSoup(r2.text, "html.parser")

    links = []

    x = soup2.select('img[src]')

    for img in x:
        links.append(img['src'])

    return Common_Strings(links)

# ? Implementation
if __name__ == "__main__":
    pass
