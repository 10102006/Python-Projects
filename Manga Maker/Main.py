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

def ExctractSeries(main_url, series_name, number_of_chapters=2, startingChapter=0):
  """
  """
  startingChapter = 31
  list_manga_links = [f'{main_url[:-1]}{index + startingChapter + 1}/' for index in range(number_of_chapters - 1)]


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
  url = 'https://read.one-punchman.com/manga/one-punch-man-chapter-/'
  ExctractSeries(url,'One_Punch_Man', 138)

