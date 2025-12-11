import win32api, win32con , time, keyboard
running = True
def failsafe():
    global running
    if keyboard.is_pressed('/'):
        running = False
def click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def reposition():
    win32api.mouse_event(win32con.MOUSE_MOVED,0,-1000)
    time.sleep(0.05)
    win32api.mouse_event(win32con.MOUSE_MOVED,0,350)
def rightclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(0.001)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
def setup():
    #first coin
    keyboard.press('s')
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSE_MOVED,0,-45)
    rightclick()
    time.sleep(0.1)
    keyboard.release('s')
    win32api.mouse_event(win32con.MOUSE_MOVED,0,45)
    time.sleep(0.1)
    #second coin
    keyboard.press('w')
    win32api.mouse_event(win32con.MOUSE_MOVED,0,75)
    time.sleep(0.1)
    rightclick()
    time.sleep(0.1)
    keyboard.release('w') 
    win32api.mouse_event(win32con.MOUSE_MOVED,0,-60)
def shoot():
    keyboard.press_and_release('4')
    time.sleep(0.17)
    click()
    time.sleep(0.1)
    keyboard.press_and_release('1')
    time.sleep(0.1)
    keyboard.press_and_release('e')
    time.sleep(0.1)
    
    win32api.mouse_event(win32con.MOUSE_MOVED,0,-350)
    time.sleep(0.2)
    #punch coin
    keyboard.press_and_release('f')
    time.sleep(0.1)
    win32api.mouse_event(win32con.MOUSE_MOVED,0,350)
    #throw coin 3 and 4
    rightclick()
    time.sleep(0.35) #0.35s
    rightclick()


while running:
    time.sleep(0.01)
    if keyboard.is_pressed('t'):
        reposition()
        setup()
        shoot()
    failsafe()
    