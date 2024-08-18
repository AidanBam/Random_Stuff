import \
    tkinter as tk  #Import tkinter so I can have a gui and import it as tk, so I don't have to write tkinter. every time
from tkinter import *
#import time #Import time bc I might need it
##Importing stuff
import random

class Windows(tk.Tk):
    def __init__(self):
        super().__init__()

        menu = Menu(self)
        self.config(menu=menu)
        settings = Menu(menu)
        menu.add_cascade(label='Settings', menu=settings)
        colours = Menu(menu)
        colours.add_cascade(label='Black background', command=self.set_black)
        colours.add_cascade(label='White background', command=self.set_white)
        colours.add_cascade(label='Grey background', command=self.set_grey)
        settings.add_cascade(label='Colours', menu=colours)
        settings.add_separator()
        settings.add_command(label='Exit', command=self.quit)

    def set_black(self):
        self.configure(bg='black')  # Change the background color to black
        self.option_add('*Background', 'black')  # Change the background color of all child widgets
        self.option_add('*Foreground', 'white')  # Change the text color of all child widgets
    def set_white(self):
        self.configure(bg='white')
        self.option_add('*Background', 'white')  # Change the background color of all child widgets
        self.option_add('*Foreground', 'black')  # Change the text color of all child widgets
    def set_grey(self):
        self.configure(bg='grey')
        self.option_add('*Background', 'grey')  # Change the background color of all child widgets
        self.option_add('*Foreground', 'black')  # Change the text color of all child widgets
class UserWindow(Windows):
    def __init__(self):
        super().__init__()
        self.title("Python Quiz")
        self.state('zoomed')

    def start_quiz(self):
        for i in range(10):
            print('Question ', i)

class Own_Work(UserWindow):
    def __init__(self):
        super().__init__()
        self.v = tk.IntVar()
        self.frame = tk.Frame(self)
        self.frame.pack(pady=20)

        self.label = tk.Label(self.frame, text="Is this all your own work?", font=("arial", 14, "bold"))
        self.label.pack(side=tk.LEFT, padx=10)

        self.radio_frame = tk.Frame(self.frame)
        self.radio_frame.pack(side=tk.LEFT)

        self.yes_radio = tk.Radiobutton(self.radio_frame, text="Yes", variable=self.v, value=1, font=("Arial", 14), indicatoron=0, width=10, padx=10, pady=10)
        self.yes_radio.pack(side=tk.LEFT)

        self.no_radio = tk.Radiobutton(self.radio_frame, text="No", variable=self.v, value=2, font=("Arial", 14), indicatoron=0, width=10, padx=10, pady=10)
        self.no_radio.pack(side=tk.LEFT)

        self.submit_button = tk.Button(self, text="Submit", command=self.get_selected_value, font=("Arial", 14), padx=20, pady=10)
        self.submit_button.pack(pady=20)

    def get_selected_value(self):
        selected_value = self.v.get()
        if selected_value == 1:
            self.yes_radio.forget()
            self.no_radio.forget()
            self.label.forget()
            self.submit_button.forget()
            self.frame.forget()
            MultipleChoiceQuestions()

        elif selected_value == 2:
            exit()

    def display_next_question(self, question_text):
        self.next_question_label.config(text=question_text)

class MultipleChoiceQuestions(UserWindow):
    def __init__(self):
        answer_key = {
            "Q1": "A",
        }
        rnd_number = int(1)
        print(answer_key["Q" + str(rnd_number)])









if __name__ == "__main__":
    window = Own_Work()
    window.mainloop()


#normal, iconic, withdrawn, or zoomed