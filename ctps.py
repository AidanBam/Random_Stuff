import ctypes
import pyautogui


class mouse:

    @staticmethod
    def click_types():
        print("L or 1 = Left click")
        print("R or 2 = Right click")
        print("M or 3 = Middle click")

    @staticmethod
    #DONE
    def set_position(x: int, y: int):
        '''Sets the position of the mouse to x, y position provided based off of pixels on screen'''
        if x < 0 or y < 0:
            print("\033[91mTypeError: x or y cannot be negative\nCurrent x =", x, "\nCurrent y =", y)
            exit()
        try:
            ctypes.windll.user32.SetCursorPos(x, y)
        except NameError:
            print("\033[91mNameError: Make sure x and y are defined")
            exit()
        except all:
            print("\033[91mSyntaxError: Unknown Error in function mouse.set_position")
            exit()

    @staticmethod
    #TODO
    def click(click_type: str or int):
        if click_type == "L" or click_type == 1:
            ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0), ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
        elif click_type == "R" or click_type == 2:
            ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0), ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
        elif click_type == "M" or click_type == 3:
            ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0), ctypes.windll.user32.mouse_event(4, 0, 0, 0, 0)
        else:
            raise ValueError("Click function is an unexpexted value", click_type, "Use mouse.click_types to see all click types")

class bypass:
    pass