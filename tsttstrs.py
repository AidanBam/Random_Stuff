from tkinter import *
root = Tk()
root.geometry('250x200+250+200')
Label(root, text="Position 1 : x=0, y=0", bg="#AFFA00", fg="white").place(x=100, y=0)
Label(root, text="Position 2 : x=50, y=40", bg="#3300CC", fg="white").place(x=50, y=40)
Label(root, text="Position 3 : x=75, y=80", bg="#FF0099", fg="white").place(x=75, y=80)
root.mainloop()
