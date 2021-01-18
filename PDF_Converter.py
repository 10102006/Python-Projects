"""
  Overview>

"""

# @ Imports
from PIL import Image
from os import path

pdf_path = 'F://Udit Downloads'

# * Defining
def MakePdf(image_name, images_path):
    try:
        image_object = Image.open(path.join(images_path))
        image = image_object.convert('RGB')

        pdf_image_name = f'{image_name}.pdf'
        pdf_image_path = path.join(pdf_path, pdf_image_name)

        image.save(pdf_image_path)
        print(f'{pdf_image_name} made at {pdf_image_path} successful')
    except Exception as e:
        print(e)

# ? Implementation
if __name__ == "__main__":
    image_name = input('Enter Image name: ')
    image_path = input('Enter Image path: ')
    MakePdf(image_name, image_path)