###########
# IMPORTS #
###########

from tkinter import *
import tkinter as tk
import time
# Importing tkinter because tkinter is what I use to create my API
# Importing tkinter as tk, so I don't have to type tkinter everytime
import random
# importing random to generate a random number so my questions are in random order


##############
# MAIN CLASS #
##############


class Windows(tk.Tk):
    """
    This class sets the background for both of my windows to light grey
    # This helps with visibility as the white it is normally set to is really bright
    # This class inherits from the superclass 'tk.Tk' (from tkinter)
    """

    def __init__(self):
        # This line initializes an object's attributes when an instance of the class is created
        super().__init__()
        # This line is used to call the constructor of the parent class when defining a subclass
        # It is a way to initialize the attributes and methods of the parent class in the subclass
        self.configure(bg='light grey')
        # This sets the background to light grey
        self.option_add('*Background', 'light grey')
        # This sets the background of things I add like buttons to grey
        self.option_add('*Foreground', 'black')
        # This sets the font to be black


#####################
# USER WINDOW CLASS #
#####################


class UserWindow(Windows):
    # This class c
    # This line inherits from the class 'Windows'
    def __init__(self):
        # This line initializes an object's attributes when an instance of the class is created
        super().__init__()
        # This line is used to call the constructor of the parent class when defining a subclass


        ###################################
        # VARIABLES USED IN THIS FUNCTION #
        ###################################

        self.QuestionsLeft = 20
        # This creates a variable named QuestionsLeft
        # It shows how many questions are left in the quiz

        # This variable is created as an integer and converted to a string when used in text
        # Having it as an integer makes it easier to change


        #####################################
        # VARIABLES USED IN OTHER FUNCTIONS #
        #####################################

        self.question_number = -1
        self.possible_question_number = -1
        self.chosen_question_numbers = []
        self.OwnWorkLabel = None
        self.OwnWorkYes = None
        self.OwnWorkNo = None
        self.multiple_choice_questions_left = 10
        self.multiple_choice_frame = tk.Frame(padx = 100, pady = 30)
        self.user_answer = 0
        self.question_number = int(9)
        self.fill_in_the_blank_question_list = list(Fill_In_Blank_Question_Dictionary.keys())
        random.shuffle(self.fill_in_the_blank_question_list)



        # These lines define some variables that are used later in this class


        #######################
        # TKINTER SCREEN SIZE #
        #######################


        self.state('zoomed')
        # This line makes my API open in zoomed state (full screen)


        ################################
        # MAKING QUESTIONS LEFT APPEAR #
        ################################


        self.QuestionsLeftLabel = tk.Label(text="Questions Left: " + str(self.QuestionsLeft), font=('arial', 18, 'bold'))
        # This line sets QuestionsLeftLabel to exist in the memory but not on the screen
        # It exists in the memory with all the attributes added to it
        self.QuestionsLeftLabel.pack(anchor='ne')
        # This line places QuestionsLeftLabel on the screen north-east (top right) side on the screen


        #########################
        # RUNNING REST OF CODE #
        ########################


        self.own_work()
        # This line runs a function called own_work

    # todo add comments (function own_work) [lines 108-123]
    def own_work(self):
        # This line creates a function called
        self.OwnWorkFrame = tk.Frame()
        self.OwnWorkFrame.pack(side = 'top')

        self.OwnWorkLabel = tk.Label(self.OwnWorkFrame, text="Is this all your own work?", font=('arial', 20, 'bold'), pady = 20)
        self.OwnWorkLabel.pack(side = 'top')

        self.OwnWorkYes = tk.Button(self.OwnWorkFrame, text="YES", font=('arial', 20, 'bold'), command=self.clear_own_work, anchor = 'n', padx = 40)
        self.OwnWorkYes.pack(side = 'left')

        self.OwnWorkNo = tk.Button(self.OwnWorkFrame, text="NO", font=('arial', 20, 'bold'), command=self.destroy, anchor = 'n', padx = 40)
        self.OwnWorkNo.pack(side = 'right')

    # todo add comments (function clear_own_work) [lines 125-131]
    def clear_own_work(self):
        self.OwnWorkFrame.destroy()
        self.OwnWorkLabel.destroy()
        self.OwnWorkYes.destroy()
        self.OwnWorkNo.destroy()
        self.multiple_choice_questions()

    # todo add comments (function get_question_number) [lines 133-145]
    def get_question_number(self):
        while self.question_number == -1:
            self.question_number = random.randint(0, 9)

            if self.question_number not in self.chosen_question_numbers:
                self.chosen_question_numbers.append(self.question_number)

            elif len(self.chosen_question_numbers) == 10:  # All possible numbers have been exhausted
                self.question_number = -2
                self.fill_in_the_blank_questions()


            else:
                self.question_number = -1

    # todo write code (function multiple_choice_questions) [lines 147 - ]
    def multiple_choice_questions(self):
        self.answered = False

        self.user_answer = 0
        self.get_question_number()

        if len(self.chosen_question_numbers) != 10:

            question = multiple_choice_questions_list[self.question_number]
            self.answer = Multiple_Choice_Question_Dictionary[question]
            self.answer_key = question.split(';')

            self.multiple_choice_frame = tk.Frame()
            self.multiple_choice_frame.pack(side = 'top')

            self.Multiple_choice_question = tk.Label(self.multiple_choice_frame, text = self.answer_key[0])
            self.Multiple_choice_question.pack(side = 'top')

            self.Multiple_choice_answer_1 = tk.Button(self.multiple_choice_frame, text = self.answer_key[1], command = self.multiple_choice_answer_1)

            self.Multiple_choice_answer_1.pack(side = 'left')

            self.Multiple_choice_answer_2 = tk.Button(self.multiple_choice_frame, text = self.answer_key[2], command = self.multiple_choice_answer_2)
            self.Multiple_choice_answer_2.pack(side = 'left')

            self.Multiple_choice_answer_3 = tk.Button(self.multiple_choice_frame, text = self.answer_key[3], command = self.multiple_choice_answer_3)
            self.Multiple_choice_answer_3.pack(side = 'left')

            self.Multiple_choice_answer_4 = tk.Button(self.multiple_choice_frame, text = self.answer_key[4], command = self.multiple_choice_answer_4)
            self.Multiple_choice_answer_4.pack(side = 'left')
        else:
            self.fill_in_the_blank_questions()

    def multiple_choice_answer_1(self):
        self.user_answer = 1
        self.check_answer()

    def multiple_choice_answer_2(self):
        self.user_answer = 2
        self.check_answer()

    def multiple_choice_answer_3(self):
        self.user_answer = 3
        self.check_answer()

    def multiple_choice_answer_4(self):
        self.user_answer = 4
        self.check_answer()


    def check_answer(self):
        if self.answered is False:
            self.answered = True
            self.NextQuestionButton = tk.Button(text = "Next Question", pady= 40, padx = 80, anchor = NE, command = self.next_question)
            self.NextQuestionButton.pack()
            self.incorrect = tk.Label(text = "That's Incorrect The Answer Is " + self.answer_key[self.answer])
            self.correct = tk.Label(text = "That's Correct")

            if str(self.user_answer) == str(self.answer):
                self.correct.pack(side = 'top')

            else:
                self.incorrect.pack(side = 'top')

    def next_question(self):
        self.multiple_choice_frame.pack_forget()
        self.Multiple_choice_question.destroy()
        self.Multiple_choice_answer_1.destroy()
        self.Multiple_choice_answer_2.destroy()
        self.Multiple_choice_answer_3.destroy()
        self.Multiple_choice_answer_4.destroy()
        self.NextQuestionButton.pack_forget()
        self.incorrect.pack_forget()
        self.correct.pack_forget()
        self.question_number = -1
        self.QuestionsLeft -= 1
        self.QuestionsLeftLabel.destroy()
        self.QuestionsLeftLabel = tk.Label(text = "Questions Left: " + str(self.QuestionsLeft), font = ('arial', 18, 'bold'))
        self.QuestionsLeftLabel.pack(anchor='ne')
        self.multiple_choice_questions()

    def fill_in_the_blank_questions(self):
        if self.QuestionsLeft == 5:
            self.Rank_In_Order_Questions()
        self.user_answer_tk = tk.StringVar()
        print(self.fill_in_the_blank_question_list)
        print(self.QuestionsLeft)
        self.question = self.fill_in_the_blank_question_list[self.QuestionsLeft - 6]

        self.answer_key = self.question.split(';')
        self.Fill_In_Blank_Label_1 = tk.Label(text = self.answer_key[0])
        self.Fill_In_Blank_Label_1.pack()
        self.Fill_In_Blank_Fill = tk.Entry(textvariable = self.user_answer_tk)
        self.Fill_In_Blank_Fill.pack()
        self.Fill_In_Blank_Label_2 = tk.Label(text = self.answer_key[1])
        self.Fill_In_Blank_Label_2.pack()
        self.Fill_In_Blank_Submit = tk.Button(text = "Submit Answer", command = self.fill_in_blank_submit)
        self.Fill_In_Blank_Submit.pack()

    def fill_in_blank_submit(self):
        self.answer = Fill_In_Blank_Question_Dictionary[self.question]
        self.incorrect = tk.Label( text = "That's Incorrect the Answer Is " + self.answer )
        self.correct = tk.Label( text = "That's Correct" )
        self.Fill_In_Blank_Submit.destroy()
        self.Fill_In_Blank_Next_Question_Button = tk.Button(text = "Next Question", command = self.Fill_Next_Question)
        self.Fill_In_Blank_Next_Question_Button.pack()


        self.user_answer = self.user_answer_tk.get()
        print(self.user_answer)
        print(self.answer.lower())

        if self.user_answer.lower() == self.answer.lower():
            self.correct.pack()
        else:
            self.incorrect.pack()

    def Fill_Next_Question( self ):
        self.Fill_In_Blank_Next_Question_Button.destroy()
        self.Fill_In_Blank_Label_1.destroy()
        self.Fill_In_Blank_Label_2.destroy()
        self.Fill_In_Blank_Fill.destroy()
        self.QuestionsLeft -= 1
        self.QuestionsLeftLabel.destroy()
        self.QuestionsLeftLabel = tk.Label(text = "Questions Left: " + str( self.QuestionsLeft ), font = ('arial', 18, 'bold'))
        self.QuestionsLeftLabel.pack(anchor='ne')
        self.fill_in_the_blank_questions()
        self.correct.destroy()
        self.incorrect.destroy()

    def Rank_In_Order_Questions( self ):
        if self.QuestionsLeft == 0:
            print('grade')

















if __name__ == '__main__':
    #################################
    # MULTIPLE CHOICE QUESTION LIST #
    #################################

    Multiple_Choice_Question_Dictionary = {
            "What colour is the sky;Blue;Purple;Green;Pink":                    1,
            "What color is grass;Green;Blue;Pink;Purple":                       1,
            "Why is grass green;Chlorophyll;Because trees are;It wants to be;4": 1,
            "14144;1;2;3;4": 4,
            "1114414;1;2;3;4": 1,
            "1145414;1;2;3;4": 1,
            "1149414;1;2;3;4": 1,
            "1164414;1;2;3;4": 1,
            "11441994;1;2;3;4": 1,
            "114999414;1;2;3;4": 1,
            "1144999914;1;2;3;4": 1}


    ###################################
    # FILL IN THE BLANK QUESTION LIST #
    ###################################

    Fill_In_Blank_Question_Dictionary = {
            "Fill in the ; with the answer1": "blank",
            "Fill in the ; with the answer2": "blank",
            "Fill in the ; with the answer3": "blank",
            "Fill in the ; with the answer4": "blank",
            "Fill in the ; with the answer5": "blank"}

    ###############################
    # RANK IN ORDER QUESTION LIST #
    ###############################

    Rank_In_Order_Question_Dictionary = {
            "Highest to lowest number;1;2;3;4": "4321",
    }


    multiple_choice_questions_list = list(Multiple_Choice_Question_Dictionary.keys( ))
    UserWindow().mainloop()
