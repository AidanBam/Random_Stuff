import \
    tkinter as tk, random
from tkinter import *

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.configure(background='grey')
        self.option_add('*Background', 'grey')
        self.option_add('*Foreground', 'black')

class UserWindow(Window):
    def __init__(self):

        print( 'hello')




if __name__ == '__main__':
    Start = UserWindow()
    Start.mainloop()

        