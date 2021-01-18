"""
  Overview>

"""

# @ Imports
from Images_Extractor import ExtractPanels
from PDF_Converter import Solo
import os


images_path = 'F://NP DATA BACKUP\Mangas/Images/'
pdfs_path = 'F://NP DATA BACKUP\Mangas/PDFS/'

# * Defining

def ExctractSeries(main_url, series_name, extra_chapters=[], endingChapter=1, startingChapter=0):
  """
  """
  list_manga_links = [f'{main_url[:-1]}{index + startingChapter + 1}/' for index in range(endingChapter - 1)]

  if type(extra_chapters) is str:
      manga_chapter_name = f'{series_name}_Chapter_{extra_chapters}'
      pdfs_folder_path = os.path.join(pdfs_path, manga_chapter_name)

      link = f'{main_url}{extra_chapters}'

      try:
        ExtractPanels(link, images_path)

        os.chdir(pdfs_path)
        os.mkdir(manga_chapter_name)
        os.chdir(pdfs_folder_path)

        converter = Solo()

        print('-----------------------------------------')      
        converter.P_MakePdfs(images_folder_path=images_path, pdfs_folder_path=pdfs_folder_path)

        print('Files made into pdfs!')

        converter.P_Pdfs_Merger(pdfs_folder_path, manga_chapter_name)  

      except Exception as exception:
        print(exception)
        print(link)

  elif type(extra_chapters) is list:
      list_manga_links.extend(extra_chapters)

      for chapter_index, links  in enumerate(list_manga_links, startingChapter):
        manga_chapter_name = f'{series_name}_Chapter_{chapter_index}'
        pdfs_folder_path = os.path.join(pdfs_path, manga_chapter_name)

        try:
          ExtractPanels(links, images_path)

          os.chdir(pdfs_path)
          os.mkdir(manga_chapter_name)
          os.chdir(pdfs_folder_path)

          converter = Solo()

          print('-----------------------------------------')      
          converter.P_MakePdfs(images_folder_path=images_path, pdfs_folder_path=pdfs_folder_path)

          print('Files made into pdfs!')

          converter.P_Pdfs_Merger(pdfs_folder_path, manga_chapter_name)  

        except Exception as exception:
          print(exception)
          print(links)


# ? Implementation
if __name__ == "__main__":
  url = 'https://schools.aglasem.com/'
  ExctractSeries(url,'NTSE_2013', '23036')

