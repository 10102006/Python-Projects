'''
    #Summary

This method will read the pdf book or other the pdfs

Features:    
    1. Extracts texts (plain text and formatted text objects)
    2. Extract PDF forms data (pure strings and formatted text objects)
    3. Supports all PDF encodings, CMap, predefined cmaps.
    4. Extracts images and image masks as Pillow/PIL Images
    5. Allows browse any document objects, resources and extract any data you need (fonts, annotations, metadata, multimedia, etc.)
    6. Follows PDF-1.7 specification
    7. Lazy objects access allows to process huge PDF documents quite fast

Required installs:
      1. pyttsx3 => This is text to speech module version 3

'''
#  * Imports
import pyttsx3
import PyPDF2
import os

# @ Defining


def ReadBook(file):
    """
      This method will read the file in which the extracted text will be present
    """
    pass
  # * This will initalise the speech bot
    speech = pyttsx3.init()  

  # * This will read the plain text
    speech.say(file)
    speech.runAndWait()


def ExtractPageOfBook(bookfile, firstpage, secondpage=0):
    """
      This method will first open the file
      Make that pdf text into plain text format
      This function will then make the program read the plain text
    """
# ! This will change the directory of the folder so that we can acsess the pdfs in this folder
    os.chdir(
        'C://Users//udit kumar//Desktop//Coding & Bowsers//Python Codes//Projects//Audio Books')

# ! This will insure that if the second page is is null then we only need one page
    if secondpage == 0:
        secondpage = firstpage

# * This with() we will open the book specified
    with open(bookfile, 'rb') as book:
      # * This will initialise the the reader so that we can perform pdf functions
        pdfReader = PyPDF2.PdfFileReader(book)

      # ! This will iterate through the all the page then only write the page we need in a file
        for _page in range(firstpage-1, secondpage):
          # ! This will get the certain page we need of the pdf
            page = pdfReader.getPage(_page)
          # ! This will extract the text as plain text
            text = page.extractText() + 'Thank you!'

          # ? This will write the file with the extracted text
            with open(f'{bookfile}_{_page + 1}.txt', 'rw') as bookpage:
                bookpage.write(text)


# ? Execution
if __name__ == '__main__':
    ExtractPageOfBook('iemo1ps.pdf', 7)
