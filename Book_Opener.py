"""
  SUMMARY

What to do:
    1. Choose a subject
    2. Then choose a book

    import os
    os.startfile("E:\School Stuffs\Class (9)\Hindi\Sparsh\ihsp1ps.pdf")

"""

# * Imports
import os
from os.path import join
from m_FolderTree import FolderTree

# @ Defination

def Choose_From_List(p_list, placeholder_txt='Which item do you want(enter index no or name): ',symbol='.'):
    """
    """
    m_list = [item for item in p_list]
    for index, item in enumerate(m_list, 1):
        printed_str = (f'{index}{symbol} {item}')
        print(printed_str)

    print('-----------------------------------------------------')
    choosen_item = input(placeholder_txt)
    r_item = ''

    if choosen_item.isnumeric():
        r_item = m_list[int(choosen_item) - 1]
    elif choosen_item in m_list:
        r_item = choosen_item

    print('-----------------------------------------------------')
    print(r_item)
    print('-----------------------------------------------------')

    return r_item

def Main(folderpath="E:\School Stuffs\Class (9)"):
    """
    """
    os.chdir(folderpath)
    extraSubject = ['English', 'Hindi', 'Sanskrit', 'SST']

    subject = Choose_From_List(os.listdir(folderpath))

    subjectpath = os.path.join(folderpath, subject)

    if subject in extraSubject:
        os.chdir(subjectpath)
        subject_division = Choose_From_List(os.listdir())

        subjectpath = os.path.join(subjectpath, subject_division)

    os.chdir(subjectpath)
    chapters = os.listdir()

    chapter = Choose_From_List(chapters)
    chapter_path = os.path.join(subjectpath, chapter)

    os.startfile(chapter_path)

# ? Implementation
if __name__ == "__main__":
    Main()
