'''
    #Summary

# $ Hey Udit from future a make some changes

# ? These are the changes
    4. Add a marking system

Database = {
  question id: {
    question: 'Pick one?',
    answer: b,
    options:[a, b, c, d]
  }
}

Things Done:
    1. MakeQuestion(question, options, answer) =>
        This will make a dict with the attributes as the params and then it will return the dict.

    2. SaveQuestion(d_question, fn_question, folder, makefolder) =>
        This will make a file using the dict format from the above function,
        this can also make a seperate folder with the file inside it
        This will make the file data in a raw format using the dict values.

    3. RetrieveQuestion(fn_question, folder) => 
        This function will retrieve the raw data from the file made by the above function.
        Then this will make the raw data into a dict which can be stored since that will be returned and added to the database dict

    4. DisplayQuestion(_question) => 
        This function will display the question in the console.
        But this function need the the question format to display the question
        * Check bellow how it is made

'''

# * Imports
import os
from os import path
import pickle


rootdir = os.getcwd()
databasedir = path.join(rootdir, 'MCQ Quesionarie\Database')


# @ Defining

Database = {}

class Pickle():
    """
    """
    def __init__(self, directory):
            """
                So this functions makes a class a constructor
            """
            self.directory = path.join(directory)
            os.chdir(directory)
    
    def StorePickleFile(data, filename):
        """
        What is done:
            1. filename confirmation this will add the '.pkl' format if the format is not avail
            2. Then we will make a file with the filename with binary encoding
            3. When the file is made then we will add the data to the file
        """
        filename = filename if '.pkl' in filename else f'{filename}.pkl'
        with open(filename, 'wb') as file:
            pickle.dump(data, file)

    def RetrievePickleFile(filename):
        """
        What is done:
            1. Filename confirmation this will add the '.pkl' format if the format is not in the given filename
            2. Then we will open the file with the given filename in read mode
            3. Then using the pickle module we will retrieve the data
            4. We will store this data and return it
        """
        filename = filename if '.pkl' in filename else f'{filename}.pkl'
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            return data

class Questionarie:
    @staticmethod
    def MakeQuestion(question, options, answer):
        """
            What is done:
                1. This function will make a dict with the attributes as the params.
                2. Params =>
                    1. question is the question which will be specified
                    2. options this will be a list containig the options of the question
                    3. answer will be one of the options which is the correct answer to the question
                
                3. This will make a var question inside the dict this will be the.dispayed question.
                4. This function will also check if the answer is present in the options array.
                5. If the above is true then the question dict will be returned.
        """

        # @ This is the question database
        t_question = {
            'question': question,
            'options': options,
            'answer': answer
        }

        # * Here we are checking if the answer is present in the options
        if answer in options:
            Database[question] = t_question
            return t_question
        else:
            print('Invaild answer pls check!')


    @staticmethod
    def SaveQuestion(d_question, fn_question, folder='', shouldMakeFolder=False):
        """
            What is done:
                1. This function basically makes the file using the dict formed from above.
                2. Params =>
                    1. {d_question} is the dict from the above function.
                    2. {fn_question} is the file name of the question.
                    3. {folder} this is the name of the folder you want to store the file in.
                    4. {makefolder} this param is dependent on the above param as this will make the folder with the {folder} name.
                3. This will first check to make a folder if {folder} is specified and {makefolder = true}.
                4. Then it will get into the folder specified.
                5. Making the file either inside a folder or root database with name {fn_question}.
                6. Adding the dict values to the file => we will add the the question, answer and options inside the file.
                7. Check how to writing of the file is done
        """
      # $ We will be checking if we should make folder or not
        if shouldMakeFolder:
            os.mkdir(path.join(databasedir, folder))

      # ? This is the main try-except
        try:
            # * this is the shorthand if where we will change the dir to the folder dir
            os.chdir(path.join(databasedir, folder)
                    ) if folder else os.chdir(databasedir)
        except:
            # ? This is the exception print statement
            print("Folder don't exist! please make the folder via function!")
      # @ This will occur when the changing of the dir is done
        finally:
            try:
                # ? Making file in the database or the specfied folder
                with open(f'{fn_question}.txt', 'w') as f_question:
                    pass
            finally:
                # ? Opening the file to write in it
                with open(f'{fn_question}.txt', 'r+') as f_question:
                    f_question.write(f"{d_question.get('question')} \n")

                    for option in d_question.get('options'):
                        f_question.write(f'\n{option}')

                    f_question.write(f"\n\n{d_question.get('answer')}")


    def RetriveQuestion(self, fn_question, folder=''):
        """
            What is done:
                1. Changing to database directory
                2. Or changing to the folder dir if specified
                3. Opening the question file with read mode
                4. Obtaining the texts
                    1. First line will be the question(* we are splicing the last two char of the string which is new line)
                    2. Obtaining the options
                        1. Looping with a fixed max options
                        2. Initialsing the each line after this, untill the line ends meaning that the options have finished
                        3. When the line ends we will break this loop for options
                    3. The like the questions we will take the answer and splice it
                5. We will store all this str in vars
                6. Then we will make a question using MakeQuestion() => param as the stored vars
                7. We will store the returned dict from MakeQuestion()
                8. Then we will return this dict
        """
        # @ Changing the dir to the root database
        os.chdir(databasedir)
        try:
            if folder:
                os.chdir(path.join(databasedir, folder))

        except:
            print("Folder don't exist! please make the folder via function!")

        with open(f'{fn_question}.txt', 'r') as f_question:
            # * This will retrieve the question but the last two char will be left
            question = (f_question.readline())[:-1]

            # $ this is just a dummy leave
            f_question.readline()

            # @ This will contain the the options
            options = []

            # * In this loop we will get the option and also remove the end /n char
            while True:
                option = (f_question.readline())[:-1]

                # * This will ensure that if option is empty then we will break out of loop
                if option:
                    options.append(option)
                else:
                    break

          # @ This readline will get the last line of the file which is the answer
            answer = f_question.readline()

          # ? This is the dict question which is returned from the MakeQuestion()
            _question = self.MakeQuestion(question, options, answer)
            return _question


    @staticmethod
    def DisplayQuestion(d_question):
        """
         What is done:
            1. Printing the main question
            2. Printing the options in a for loop
            3. Also making an index with enumerate
            4. Initialising the answer index by checking with the index of the options
            5. Asking for input as the question number
            6. Checking the input number with the answer number
        """
        # $ Here we are printing the main question
        print(d_question.get('question'))

      # ? Here I am storing the options from the dict in a seperate var
        options = d_question.get('options')

      # @ Here I am intialising the n_answer which will be the index number of the which is correct
        n_answer = 0

      # * Here I am looping through the options list with an index - i
        for i, option in enumerate(options):
            print(f'{i + 1}) {option}')

          # * Here I am checking if the option is the answer if yes then the index will also be the answer so I am setting the n_answer as the i
            if option == d_question.get('answer'):
                n_answer = (i + 1)

        while True:
            i_answer = int(input('Your answer number: '))
            if i_answer == n_answer:
                # $ Change this so it will work as marking
                print('Your answer is correct!')
                print('-----------------------------------------')
                return
            else:
                print('Incorrect, try again!')
                print('-----------------------------------------')

class New_Questionarie(Pickle):
    @staticmethod
    def MakeQuestion(question, options, answer):
        """
            What is done:
                1. This function will make a dict with the attributes as the params.
                2. Params =>
                    1. question is the question which will be specified
                    2. options this will be a list containig the options of the question
                    3. answer will be one of the options which is the correct answer to the question
                
                3. This will make a var question inside the dict this will be the.dispayed question.
                4. This function will also check if the answer is present in the options array.
                5. If the above is true then the question dict will be returned.
        """

        # @ This is the question database
        t_question = {
            'question': question,
            'options': options,
            'answer': answer
        }

        # * Here we are checking if the answer is present in the options
        if answer in options:
            Database[question] = t_question
            return t_question
        else:
            print('Invaild answer pls check!')

    @staticmethod
    def SaveQuestion(d_question, fn_question, folder='', shouldMakeFolder=False):
        """
            What is done:
                1. This function basically makes the file using the dict formed from above.
                2. Params =>
                    1. {d_question} is the dict from the above function.
                    2. {fn_question} is the file name of the question.
                    3. {folder} this is the name of the folder you want to store the file in.
                    4. {makefolder} this param is dependent on the above param as this will make the folder with the {folder} name.
                3. This will first check to make a folder if {folder} is specified and {makefolder = true}.
                4. Then it will get into the folder specified.
                5. Making the file either inside a folder or root database with name {fn_question}.
                6. Adding the dict values to the file => we will add the the question, answer and options inside the file.
                7. Check how to writing of the file is done
        """
      # $ We will be checking if we should make folder or not
        if shouldMakeFolder:
            os.mkdir(path.join(databasedir, folder))

      # ? This is the main try-except
        try:
            # * this is the shorthand if where we will change the dir to the folder dir
            os.chdir(path.join(databasedir, folder)
                    ) if folder else os.chdir(databasedir)
        except:
            # ? This is the exception print statement
            print("Folder don't exist! please make the folder via function!")

      # @ This will occur when the changing of the dir is done
        finally:
            try:
                # ? Making file in the database or the specfied folder
                Pickle.StorePickleFile(d_question, fn_question)

            except Exception as e:
                print(e)


    @staticmethod
    def RetriveQuestion(fn_question, folder=''):
        """
            What is done:
                1. Changing to database directory
                2. Or changing to the folder dir if specified
                3. Opening the question file with read mode
                4. Obtaining the texts
                    1. First line will be the question(* we are splicing the last two char of the string which is new line)
                    2. Obtaining the options
                        1. Looping with a fixed max options
                        2. Initialsing the each line after this, untill the line ends meaning that the options have finished
                        3. When the line ends we will break this loop for options
                    3. The like the questions we will take the answer and splice it
                5. We will store all this str in vars
                6. Then we will make a question using MakeQuestion() => param as the stored vars
                7. We will store the returned dict from MakeQuestion()
                8. Then we will return this dict
        """
        # @ Changing the dir to the root database
        os.chdir(databasedir)
        try:
            if folder:
                os.chdir(path.join(databasedir, folder))

        except:
            print("Folder don't exist! please make the folder via function!")

        d_question = Pickle.RetrievePickleFile(fn_question)
        return d_question

    @staticmethod
    def DisplayQuestion(d_question):
        """
         What is done:
            1. Printing the main question
            2. Printing the options in a for loop
            3. Also making an index with enumerate
            4. Initialising the answer index by checking with the index of the options
            5. Asking for input as the question number
            6. Checking the input number with the answer number
        """
        # $ Here we are printing the main question
        print(d_question.get('question'))

      # ? Here I am storing the options from the dict in a seperate var
        options = d_question.get('options')

      # @ Here I am intialising the n_answer which will be the index number of the which is correct
        n_answer = 0

      # * Here I am looping through the options list with an index - i
        for i, option in enumerate(options):
            print(f'{i + 1}) {option}')

          # * Here I am checking if the option is the answer if yes then the index will also be the answer so I am setting the n_answer as the i
            if option == d_question.get('answer'):
                n_answer = (i + 1)

        while True:
            i_answer = int(input('Your answer number: '))
            if i_answer == n_answer:
                # $ Change this so it will work as marking
                print('Your answer is correct!')
                print('-----------------------------------------')
                return
            else:
                print('Incorrect, try again!')
                print('-----------------------------------------')


# ? Execution
if __name__ == '__main__':
    questionaire = New_Questionarie(databasedir)

    # r_question = questionaire.MakeQuestion('How is Udit?',['Good', 'Bad', 'Fat', 'Old'], 'Good')

    # questionaire.SaveQuestion(r_question, 'nature', 'WhatDoYaThin', True)
    
    r_question = questionaire.RetriveQuestion('Udit')
    questionaire.DisplayQuestion(r_question)

