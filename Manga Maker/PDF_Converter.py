
"""
  Overview

"""

# @ Imports
from PIL import Image
import os
from os import path
from PyPDF2 import PdfFileMerger


# * Defining
images_path = path.join('F:/Android/android-sdk/Mangas/Images')
pdfs_path = path.join('F:/Android/android-sdk/Mangas/PDFS')

def MakePdf(image_name, images_path, pdfs_path):
    image_object = Image.open(path.join(images_path, image_name))
    image = image_object.convert('RGB')

    pdf_image_name = f'{image_name[:-4]}.pdf'
    pdf_image_path = path.join(pdfs_path, pdf_image_name)

    image.save(pdf_image_path)

def MakePdfs(images_folder_path, pdfs_folder_path):
    list_images = os.listdir(images_folder_path)

    for image in list_images:
        MakePdf(image, images_folder_path, pdfs_folder_path) 

def Pdfs_Merger(pdfs_folder_path, filename):
    """
    """
    os.chdir(pdfs_folder_path)
    pdfs = os.listdir()

    merger = PdfFileMerger()

    for pdf in pdfs:
        merger.append(pdf) 

    merger.write(filename + '.pdf')
    merger.close()

# ? Implementation
if __name__ == "__main__":
    MakePdfs(images_path, pdfs_path)
    Pdfs_Merger(pdfs_path, 'wallpapers')