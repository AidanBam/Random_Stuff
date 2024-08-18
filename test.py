import tkinter as tk

class windows(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Python Quiz")
        self.overrideredirect(True)  # Remove the default window decorations

        # Create a custom title bar
        self.title_bar = tk.Frame(self, bg='blue', relief='raised', bd=2)
        self.title_bar.pack(fill='x')

        # Add the window title to the title bar
        self.title_label = tk.Label(self.title_bar, text="Python Quiz", bg='blue', fg='white')
        self.title_label.pack(side='left', padx=10)

        # Add the close button to the title bar
        self.close_button = tk.Button(self.title_bar, text='X', command=self.quit, bg='red', fg='white')
        self.close_button.pack(side='right', padx=10)

        # Add the minimize button to the title bar
        self.minimize_button = tk.Button(self.title_bar, text='_', command=self.iconify, bg='green', fg='white')
        self.minimize_button.pack(side='right')

        # Bind mouse events to move the window
        self.title_bar.bind('<B1-Motion>', self.move_window)
        self.title_bar.bind('<ButtonRelease-1>', self.release_window)

        # Keep track of the window position
        self.window_x = 0
        self.window_y = 0

    def move_window(self, event):
        self.window_x = event.x
        self.window_y = event.y
        self.geometry(f'+{event.x_root}+{event.y_root}')

    def release_window(self, event):
        self.window_x = None
        self.window_y = None

if __name__ == "__main__":
    root = windows()
    root.mainloop()