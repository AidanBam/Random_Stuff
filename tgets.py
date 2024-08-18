import pyautogui
import ctypes
import time
def open_roblox():
    pyautogui.PAUSE = (3)
    pyautogui.click(345, 787)
    i = 1
    while i==1:
        if pyautogui.pixelMatchesColor( 267, 798, (255, 158, 54) ):  # jailbreak appears
            pyautogui.click( 267, 798 )
            i=2
            while i==2:
                if pyautogui.pixelMatchesColor(660, 459, (0, 176, 111), tolerance = 20 ):  # play appears
                    pyautogui.click( 657, 458 )
                    i=3
                    while i==3:
                        if pyautogui.pixelMatchesColor( 112, 102, (28, 20, 28), tolerance = 10 ):  # script appears
                            run_script()
                            pyautogui.moveTo(0,0, 10)
                            i=4


def run_script():
    print( "running" )
    pyautogui.click( 120, 422 )
    pyautogui.PAUSE = 0.1
    pyautogui.click(1590, 953)
    pyautogui.PAUSE = 0.1
    pyautogui.click( 1774, 960 )
    pyautogui.PAUSE = 0.1
    pyautogui.click( 120, 420 )
    pyautogui.PAUSE = 0.1
    i=1

while True:
    try:
        end = time.time( )
        i=1
        pyautogui.PAUSE = 5
        print(ctypes.windll.user32.GetKeyState(0x1B))
        if ctypes.windll.user32.GetKeyState(0x1B) != 0:
            break
        elif not pyautogui.pixelMatchesColor( 239, 19, (192, 201, 212) ): #roblox closed
            print(pyautogui.pixel(239, 19))
            open_roblox()
            start = time.time()
        elif pyautogui.locateOnScreen( 'error.png', confidence = 0.7 ):
            pyautogui.click(417, 19)
        elif pyautogui.locateOnScreen('jailbreak.png', confidence =  0.1):
            pyautogui.click( 417, 19)
        elif end - start >= 1200:
            pyautogui.click( 417, 19)


    except:
        print("not found")


