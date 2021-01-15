"""
  Overview>

"""

# @ Imports
from bs4 import *
import requests as rq
import os

# * Defining
url = 'https://w11.tenseishitaraslimedattaken-manga.com/manga/tensei-shitara-slime-datta-ken-chapter-28/'

def ExtractPanels(url, images_folder_path, commonlink=''):
    """
    """
    r2 = rq.get(url)
    soup2 = BeautifulSoup(r2.text, "html.parser")

    links = []

    x = soup2.select(f'img[src^={commonlink}]' if commonlink else 'img[src]')

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

def Extract_Print_Panels(url):
    """
    """
    pass
    r2 = rq.get(url)
    soup2 = BeautifulSoup(r2.text, "html.parser")

    links = []

    x = soup2.select('img[src]')

    for img in x:
        links.append(img['src'])

    for link in links:
        print(link)

# ? Implementation
if __name__ == "__main__":
    Extract_Print_Panels(url)