
"""
  Overview

"""

# @ Imports
from PIL import Image
import os
from os import path
from PyPDF2 import PdfFileMerger


# * Defining
images_path = path.join('F://NP DATA BACKUP\Mangas\Images/')
pdfs_path = path.join('F://NP DATA BACKUP\Mangas/PDFS/')
# pdfs_path = path.join('F:\Android\android-sdk\Mangas\PDFS\Chapter1')

class Main():
    """
    """

    @staticmethod
    def MakePdf(image_name, images_path, pdfs_path):
        image_object = Image.open(path.join(images_path, image_name))
        image = image_object.convert('RGB')

        pdf_image_name = f'{image_name[:-4]}.pdf'
        pdf_image_path = path.join(pdfs_path, pdf_image_name)

        image.save(pdf_image_path)

    def MakePdfs(self, images_folder_path, pdfs_folder_path):
        list_images = os.listdir(images_folder_path)

        for image in list_images:
            self.MakePdf(image, images_folder_path, pdfs_folder_path) 

    @staticmethod
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

        list_images = os.listdir(images_path)

        for image in list_images:
            os.remove(f'{images_path}{image}')

        for pdf in pdfs:
            os.remove(f'{pdfs_path}{pdf}')

class Solo():
    @staticmethod
    def P_MakePdf(image_name, images_path, pdfs_path):
        image_object = Image.open(path.join(images_path, image_name))
        image = image_object.convert('RGB')

        pdf_image_name = f'{image_name[:-4]}.pdf'
        pdf_image_path = path.join(pdfs_path, pdf_image_name)

        image.save(pdf_image_path)

    def P_MakePdfs(self, images_folder_path, pdfs_folder_path):
        list_images = os.listdir(images_folder_path)

        for image in list_images:
            self.P_MakePdf(image, images_folder_path, pdfs_folder_path) 
            print(f'{f"{image[:-4]}.pdf"} sucessfully made! > P_MakePDFS')
        print('--------------------------------------------------------')

    @staticmethod
    def P_Pdfs_Merger(pdfs_folder_path, filename):
        """
        """
        os.chdir(pdfs_folder_path)
        pdfs = os.listdir()

        merger = PdfFileMerger()

        for pdf in pdfs:
            if not path.isdir(path.join(pdfs_folder_path, pdf)):
                print(f'{pdf} is merged with {filename}')
                merger.append(pdf)
        print('--------------------------------------------------------')

        merger.write(filename + '.pdf')
        merger.close()

        print(f'{filename} sucessfully made!')
        print('--------------------------------------------------------')

        list_images = os.listdir(images_path)

        for image in list_images:
            os.remove(f'{images_path}{image}')
            print(f'{image} sucessfully removed!')
        print('--------------------------------------------------------')

        # for pdf in pdfs:
        #     os.remove(f'{pdfs_path}{pdf}')
        #     print(f'{pdf} sucessfully removed!')
        # print('--------------------------------------------------------')


# ? Implementation
if __name__ == "__main__":
    converter = Solo()
    converter.P_MakePdfs(images_path, pdfs_path)
    converter.P_Pdfs_Merger(pdfs_path, 'Chapter 128')