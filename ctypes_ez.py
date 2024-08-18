import ctypes
import subprocess
import time


class ctp:
    class mouse:
        class extended:
            def mouse_set_position(self):
                try:
                    print(x, y)
                    ctypes.windll.user32.SetCursorPos(x, y)
                    return True
                except NameError:
                    print("make sure x and y are defined")
                finally:
                    print("mouse_set_position error")

            def left_click_down(self):
                ctypes.windll.user32.mouse_event(2, 0, 0, 0, 0)
                return True
            def left_click_up(self):
                ctypes.windll.user32.mouse_event( 4, 0, 0, 0, 0 )
                return True
z = None
y = 300
ctp.mouse.extended.mouse_set_position(z)
ctp.mouse.extended.left_click_down(z)
ctp.mouse.extended.left_click_up(z)

