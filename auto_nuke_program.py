import win32api, win32con , time, keyboard
shotgun_equipped = False
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def nuke():
    
    keyboard.press_and_release('4')
    time.sleep(0.1)
    keyboard.press_and_release('e')
    time.sleep(0.01)
    click()
    keyboard.press_and_release('left_shift')
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,0,350)
def charge():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.35)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,0,-1000)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
    time.sleep(0.01)
    nuke()

while True:

    if keyboard.is_pressed('/'):
        break
    elif keyboard.is_pressed('1') or keyboard.is_pressed('3') or keyboard.is_pressed('4') or keyboard.is_pressed('5'):
        shotgun_equipped = False
    elif keyboard.is_pressed('2'):
        shotgun_equipped = True
    elif keyboard.is_pressed('t') and shotgun_equipped == False:
        
        keyboard.press_and_release('2')
        time.sleep(0.1)
        charge()

        #shotgun_equipped= True
    elif keyboard.is_pressed('t') and shotgun_equipped == True:
        time.sleep(0.1)
        charge()
        shotgun_equipped = False