import time, win32api, win32con, keyboard
def right_click():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
def move_mouse(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,x,y)
    time.sleep(0.01)
def swap_weapons(pinput:str,How_many_times:int): # makes swapping easier
    allowed = ["1","2","3","4","5"]
    condition_is_in_list = False
    for i in allowed:# validates it makes debugging easier
        if i == pinput:
            condition_is_in_list = True
    if condition_is_in_list:
        for i in range(0,How_many_times):
            keyboard.press_and_release(pinput)
            time.sleep(0.01)
def dashjump():
    keyboard.press_and_release("shift")
    time.sleep(0.01)
    keyboard.press_and_release("space")
def slide(Seconds:float):
    keyboard.press("control")
    time.sleep(Seconds)
    keyboard.release("control")
def walk(pinput:str,Seconds:float):
    allowed = ["w","d","a","s"]
    for i in allowed: # validates it makes debugging easier
        if i == pinput:
            condition_is_in_list = True
    if condition_is_in_list:
        keyboard.press(pinput)  
        time.sleep(Seconds)
        keyboard.release(pinput)

def main():
    #reset weapons
    swap_weapons("1",1)

    swap_weapons("2",1)

    swap_weapons("1",2)

    #speedrun begins
    dashjump()
    time.sleep(0.994)
    right_click()
    time.sleep(0.003)
    move_mouse(45,0)
    time.sleep(0.1)
    keyboard.press_and_release("shift")
    time.sleep(0.25)
    slide(0.0965)
    walk("w",0.34)
    time.sleep(0.001)
    slide(0.001)
    



    

while True:
    if keyboard.is_pressed("t"):
        main()
    else:
        time.sleep(0.001)