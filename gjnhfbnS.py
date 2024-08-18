print("hoi")

import random
import \
    tkinter as tk, random
from tkinter import *


class Windows(tk.Tk):

    def __init__(self):
        super().__init__()
        self.configure(bg='light grey')
        self.option_add('*Background', 'light grey')
        self.option_add('*Foreground', 'black')


class UserWindow(Windows):

    def __init__(self):

        super().__init__()
        self.state('zoomed')
        self.QuestionsLeftLabel = tk.Label(text="Questions Left: " + str(QuestionsLeft), font=('arial', 16, 'bold')).place(x=1720, y=15)
        self.own_work()


    def own_work(self):
        self.OwnWorkLabel = tk.Label(text="Is this all your own work?", font=('arial'))
        self.OwnWorkLabel.place(relx=0.3, rely=0.1)

        self.OwnWorkYes = tk.Button(text="YES", font=('arial'), command=self.clear_own_work)
        self.OwnWorkYes.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.05)

        self.OwnWorkNo = tk.Button(text="NO", font=('arial'), command=exit)
        self.OwnWorkNo.place(relwidth=0.1,relx=0.7, rely=0.2, relheight=0.05)

    def clear_own_work(self):
        self.OwnWorkLabel.destroy()
        self.OwnWorkYes.destroy()
        self.OwnWorkNo.destroy()
        self.get_multiple_choice_question_number()
        self.multiple_choice_questions()

    def get_multiple_choice_question_number(self):
        self.multiple_choice_question_number = -1
        print('times ran')
        while self.multiple_choice_question_number == -1:
            self.possible_question_number = random.randint(0,9)

            if self.possible_question_number not in chosen_question_numbers:
                chosen_question_numbers.append(self.possible_question_number)
                self.multiple_choice_question_number = self.possible_question_number
            elif len(chosen_question_numbers) == 10:  # All possible numbers have been exhausted
                    print("error: infinite loop")
                    exit()

    def multiple_choice_questions(self):
        for i in range(0, 100):
            print(self.multiple_choice_question_number)
            print(chosen_question_numbers)
            self.get_multiple_choice_question_number()
            print(chosen_question_numbers)







if __name__ == '__main__':


    QuestionsLeft = 20
    chosen_question_numbers = []
    UserWindow = UserWindow()
    UserWindow.mainloop()

############################
#    i=0
#    question = questions[i]
#   answer = Question_Dictionary[question]
#    print(question + " " + answer)\

##MULTIPLE CHOICE QUESTION LIST##
#Question_Dictionary = {
#    "What colour is the sky": "blue",
#    "What color is grass": "green"

#}
#questions = list(Question_Dictionary.keys())