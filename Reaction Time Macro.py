import ctypes
while True:
    DC = ctypes.windll.user32.GetDC(0)
    color = tuple(int.to_bytes(ctypes.windll.gdi32.GetPixel(DC, 400, 400), 3, "little"))
    if color == (75, 219, 106):
        ctypes.windll.user32.SetCursorPos(100, 400), ctypes.windll.user32.mouse_event(2,0,0,0,0), ctypes.windll.user32.mouse_event(0,0,0,0,0)