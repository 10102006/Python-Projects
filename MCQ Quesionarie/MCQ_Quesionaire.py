'''

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
        This function will make a dict with the attributes as the params and then it will return the dict => question-object.

    2. SaveQuestion(d_question, fn_question, folder, makefolder) =>
        This will make a file using the question-object from the above function, this can also make a seperate folder with the file inside it. This will make the file data in a raw format using the dict values.

    3. RetrieveQuestion(fn_question, folder) => 
        This function will retrieve the raw data from the file made by the above function.
        Then this will make the raw data into a dict which can be stored since that will be returned and added to the database dict

    4. DisplayQuestion(_question) => 
        This function will display the question in the console. But this function need the the question format to display the question

'''

# * Imports
import os
from os import path
import pickle


root_directory = os.getcwd()
database_directory = path.join(root_directory, 'MCQ Quesionarie\Database')


# @ Defining

Database = {}


class Pickle():
    """
    This class will be used to store and retrieve the mcq files which is in the dict format
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
            1. filename confirmation: this will add the '.pkl' format if the format is not written.
            2. Then we will make a file with the filename with binary encoding.
            3. When the file is made then we will add the data to the file.
        """
        filename = filename if '.pkl' in filename else f'{filename}.pkl'

        with open(filename, 'wb') as file:
            pickle.dump(data, file)
            print(f"{filename}  is made!")

    def RetrievePickleFile(filename):
        """
        What is done:
            1. Filename confirmation: this will add the '.pkl' format if the format is not in the given filename.
            2. Then we will open the file with the given filename in read mode.
            3. Then using the pickle module we will retrieve the data. We will store this data and return it
        """
        filename = filename if '.pkl' in filename else f'{filename}.pkl'
        with open(filename, 'rb') as file:
            data = pickle.load(file)
            return data


class Questionaire(Pickle):

    def __init__(self, database_directory):
        """
            So this functions makes a class a constructor
        """
        self.database_directory = database_directory

    @staticmethod
    def MakeQuestion(question, options, answer):
        """
        What is done:
            This function will make a dict with the attributes as the params.
            1. Params =>
                1. question: is the question asked which will be specified.
                2. options: this will be a array containig the options of the question
                3. answer: will be one of the options which is the correct answer to the question

            2. This will make a question-object with all the parameters as attributes.
            3. Then we will also check if the answer is present in the options array.
            4. If the above is true then the question dict will be returned.
        """

        # @ This is the question database
        t_question = {
            "question": question,
            "options": options,
            "answer": answer
        }

        # * Here we are checking if the answer is present in the options
        if answer in options:
            Database[question] = t_question
            return t_question
        else:
            print('Invaild answer pls check!')

    @staticmethod
    def SaveQuestion(question_object, filename_question, folder_name="", should_make_folder=False):
        """
            What is done:
                This function basically makes the file using the question-object formed from above.
                1. Params =>
                    1. {question_object}: is the dict from the above function.
                    2. {filename_question}: is the filename of the question.
                *** Optional
                    3. {folder_name}: this is the name of the folder you want to store the file in.
                    4. {should_make_folder}: this param is a bool which will decide if the folder with name {folder_name} should be made.

                2. This will first check to make a folder if {folder} is specified and {should_make_folder = true}.
                3. Then it will chage_dir into the folder specified.
                4. Making the file either inside a folder or root database with name {filename_question}.
                5. We will make the file with pickle class
        """
      # ! We will be checking if we should make folder or not
        if should_make_folder:
            os.mkdir(path.join(database_directory, folder_name))

      # ? This is the main try-except
        try:
            # * this is the shorthand if where we will change the dir to the folder dir
            os.chdir(path.join(database_directory, folder_name)
                     ) if folder_name else os.chdir(database_directory)
        except:
            # ? This is the exception print statement
            print("Folder don't exist! please make the folder via function!")

        # @ This will occur when the changing of the dir is done
        else:
            try:
                # ? Making file in the database or the specfied folder
                Pickle.StorePickleFile(question_object, filename_question)

            except Exception as e:
                print(e)

    @staticmethod
    def RetriveQuestion(filename_question, folder_name=''):
        """
            What is done:
                This function will retrieve the file info with pickle class and return the question_object
                1. Changing to database directory, Or changing to the folder dir if specified.
                2. Checking if the folder is correct or not.
                3. Retrieving the file with the pickle class and returning the question_object.
        """
        # @ Changing the dir to the root database
        os.chdir(database_directory)

        try:
            if folder_name:
                os.chdir(path.join(database_directory, folder_name))
        except:
            print("Folder don't exist! please make the folder via function!")
        finally:
            question_obejct = Pickle.RetrievePickleFile(filename_question)
            return question_obejct

    @staticmethod
    def DisplayQuestion(question_object):
        """
         What is done:
            1. Printing the main question
            2. Printing the options in a for loop
            3. Also making an index with enumerate
            4. Initialising the answer index by checking with the index of the options
            5. Asking for input as the question number
            6. Checking the input number with the answer number
        """
      # @ Here we are printing the main question
        print(question_object.get("question"))

      # ? Here I am storing the options from the dict in a seperate var
        options = question_object.get("options")
        answer_index = int(options.index(question_object.get("answer"))) + 1

      # * Here I am looping through the options list with an index - i
        [print(f'{i + 1}) {option}') for i, option in enumerate(options)]

        input_answer_index = int(input('Your answer number: '))
        if input_answer_index == answer_index:
            print("Your answer is correct!")
            print('-----------------------------------------')
            return
        else:
            print("Incorrect")
            print('-----------------------------------------')


class ConsleQuestionaire(Questionaire):
    """
    MainFunction(numberOfQuestion, test-name, ):
        questions = []
        for range(numberOfQuestion):
            question = MakeQuestion() => will return an question-object
            question.append(question)
        ask to save the questions -
            - make a folder to store the questions
            - in loop save the question in the folder
    """

    def __init__(self, database_directory):
        """
            So this functions makes a class a constructor
        """
        self.database_directory = database_directory

    @staticmethod
    def MakeQuestion():
        """
        This function will make question-object in the console and then return the question-object
        """
        question = input("Enter the question:  ")

        def MakeOptions(numberOfOptions=4):
            """
            This function will make a list with all the options and  return the list 
            """
            options = []
            for _ in range(numberOfOptions):
                option = input("> ")
                options.append(option)
            return options

        options = MakeOptions()
        answer = input("Answer:  ")

        question_object = Questionaire.MakeQuestion(question, options, answer)
        return question_object

    def MakeTest(self, numberOfQuestion=0, questions=[]):
        """
        This is the main function
        """
        nameOfTest = input("Name of the test: ")

        for question_index in range(numberOfQuestion if numberOfQuestion else int(input("Enter number of question: "))):
            print('-----------------------------------------')
            question = self.MakeQuestion()
            question.update({"index": str(question_index + 1)})

            questions.append(question)
            print('-----------------------------------------')

        try:
            print(questions)
            shouldSave = True if input(
                "Should save(0 - true, 1 - false): ") == "0" else False
            if shouldSave:
                os.chdir(database_directory)
                os.mkdir(nameOfTest)

                for question in questions:
                    Questionaire.SaveQuestion(
                        question, question.get("index"), nameOfTest)

                # [Questionaire.SaveQuestion(question, question.get("index"), nameOfTest) for question in questions]
        except Exception as e:
            print(e)


# ? Execution
if __name__ == '__main__':
    questionaire = ConsleQuestionaire(database_directory)

    # _questionaire = Questionaire(database_directory)
    # questions = []
    # question1 = _questionaire.MakeQuestion("Colour of sun?", ["blue", "pink", "yellow", "green"], "yellow")
    # question2 = _questionaire.MakeQuestion("Colour of water?", ["blue", "pink", "yellow", "green"], "blue")

    # questions.append(question1)
    # questions.append(question2)

    questionaire.MakeTest()
