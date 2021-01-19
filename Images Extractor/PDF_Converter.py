
"""
  Overview

What has beeen done:
    1. Importing all the necessary modules
    2. We need two path for:
        1. First path should be of a folder were the images are stored
        2. Second where we will store the pdfs
        ** These path are for checking and debugging of code
    3. ** There are two class Main/Solo
        1. Main class will only do the job required
        2. Solo is like a documented pdf making where we will print each file names which are made pdf
    4. Main:
        1. Initialising the pdf_folder_path and image_folder_path in the class
        2. MakePdf:
            ** This function will make pdf of an image whose name is given, and is in the images folder
        3. MakePdfs:
            ** This function will make all the images in the images folder into a seperate files in the a folder specified
        4. Pdfs_Merger:
            ** This function will merge all the pdfs in a specified folder
    5. Solo:
        1. This class does the same thing as above just one difference that we ae printing all the reseults in the console as output like:
            1. What files are made into pdf
            2. What files are merged
            3. If the merged files making is success or not
        
        
"""

# @ Imports
from PIL import Image
import os
from os import path
from PyPDF2 import PdfFileMerger


# * Defining
images_path = path.join('F://NP DATA BACKUP\Mangas\Images/')
pdfs_path = path.join('F://NP DATA BACKUP\Mangas/PDFS/')

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
    def __init__(self, image_folder_path, pdf_folder_path):
        """
            So this functions makes a class a constructor
        """
        self.image_folder_path = image_folder_path
        self.pdf_folder_path = pdf_folder_path
    
    def D_MakePdf(self, pdf_folder_path, image_name):
        """
        What is done:
            1. Opening the image with PIL module
            2. Then converting the image into RGB format
            3. We will make a name for the file using f-string
            4. 
        """
        image_object = Image.open(path.join(self.image_folder_path, image_name))
        image = image_object.convert('RGB')

        image_name, _ = image_name.rsplit('.')
        pdf_image_name = f'{image_name}.pdf'

        pdf_image_path = path.join(pdf_folder_path, pdf_image_name)

        image.save(pdf_image_path)

    def P_MakePdfs(self, pdf_folder_path):
        list_images = [image[:-4] for image in os.listdir(self.images_folder_path)]
        list_images_format = [image[(len(image) - 4):] for image in os.listdir(self.images_folder_path)]

        try:
            list_images.sort(key=int)
        except:
            pass

        for image, format in zip(list_images, list_images_format):
            self.D_MakePdf(image + format, self.images_folder_path, pdf_folder_path)
            print(f'{f"{image}.pdf"} sucessfully made! > P_MakePDFS')
        print('--------------------------------------------------------')

    @staticmethod
    def D_Pdfs_Merger(pdf_folder_path, filename):
        """
        """
        os.chdir(pdf_folder_path)
        int_pdfs = [pdf[:-4] for pdf in os.listdir()]

        int_pdfs.sort(key=int)

        merger = PdfFileMerger()

        for pdf in int_pdfs:
            if not path.isdir(path.join(pdf_folder_path, pdf)):
                print(f'{pdf}.pdf is merged with {filename}')
                merger.append(pdf+'.pdf')
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
    # converter = Solo()
    # converter.D_MakePdfs(images_path, pdfs_path)
    # converter.P_Pdfs_Merger(pdfs_path, 'NTSE_2013')
    pass