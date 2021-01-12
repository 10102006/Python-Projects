'''
    # Summary

This folder is very useful as I will use this to convert image to pdf

Tasks:
      1.

'''

# * Imports
from fpdf import FPDF
import os

# @ Defining


def ConvertToPDF(image, listofimages=[]):
    """
      This function will make image into pdf
      This can also convert list of imgs to pdf
    """
# ! This will change the directory to this folder so that we can see this folders images
    os.chdir(
        'C://Users//udit kumar//Desktop//Coding & Bowsers//Python Codes//Projects//PDF Converter')
    img = Image.open('image.png')
    print(img.size)
#     pdf = FPDF()
#     try:
#         pdf.add_page()
#         pdf.image(image, 500, 500, 500, 500)
#         pdf.output(f"{image}.pdf", "F")
#         print('Your image has been converted to pdf!')
#     except Exception as exception:
#         print(exception)


# ? Execution
if __name__ == '__main__':
    ConvertToPDF('CEA format2.png')
