"""
  Overview>

"""

# @ Imports
from docx import Document

# * Defining

# ? Implementation
if __name__ == "__main__":
  document = Document()
  document.save('test.docx')
