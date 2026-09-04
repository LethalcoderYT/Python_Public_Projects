import time,win32api,win32con,keyboard
#constants
COOLDOWN = 0.01
EVEN_SHORTER_COOLDOWN = 0.001
LONG_COOLDOWN = 0.1
HOTKEY = "t" # to activate the program after running
MALICIOUS_RAILGUN_SLOT = 2 # change this depending where you put the railgun slot for malcious rail cannon
CORE_EJECT_SHOTGUN_SLOT = 1 # same with the one above but for shotgun
BLUE_ROCKET_SLOT = 1
RED_ROCKET_SLOT = 2
KNUCKLE_BLASTER_HOTKEY = "g" # assumes it has one so change the constant below to False and knuckleblaster is pre-equipped
HAS_HOTKEY_FOR_KNUCKLE_BLASTER = True
#global variables

#functions
#mouse controls
def leftclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(COOLDOWN)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def hold_rightclick(seconds:float):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    time.sleep(seconds)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
def move_mouse(x_distance,y_distance):
    win32api.mouse_event(win32con.MOUSE_MOVED,x_distance,y_distance)
#keyboard controls
def switch_weapon(weapon:int):
    valid_inputs = [1,2,3,4,5]
    valid = False
    for item in valid_inputs:
        if item == weapon:
            weapon = str(weapon) # allows keyboard module to use it
            valid = True
            break
    if valid:
        keyboard.press_and_release(weapon)
    else:
        print(f"{weapon} isn't valid weapon slot")
def reset_weapons():
    switch_weapon(3)
    time.sleep(EVEN_SHORTER_COOLDOWN)
    switch_weapon(4) # makes 100% sure 
    time.sleep(EVEN_SHORTER_COOLDOWN)
    for i in range (0,CORE_EJECT_SHOTGUN_SLOT):
        switch_weapon(2) # switches to core eject shotgun
        time.sleep(EVEN_SHORTER_COOLDOWN)

#key pressing
def hold_and_release_key(key:str,cooldown:float): # holds key for a specific amount of time before realsing it
    keyboard.press(key)
    time.sleep(cooldown)
    keyboard.release(key)

#movement
def dash():
    keyboard.press_and_release("shift")
def dashjump():
    dash()
    time.sleep(COOLDOWN+0.05)
    keyboard.press_and_release("SPACE")

# sequence of exucution
def main_sequence():
    reset_weapons() # makes sure start of speedrun automatically is set to the core eject shotgun
    hold_and_release_key("w",1)
    time.sleep(COOLDOWN)
    dashjump()
    time.sleep(1)
    move_mouse(595,-50) #605
    hold_rightclick(LONG_COOLDOWN)
    time.sleep(LONG_COOLDOWN)
    move_mouse(0,50)
    for i in range(0,MALICIOUS_RAILGUN_SLOT):
        switch_weapon(4)
        time.sleep(COOLDOWN)
    
    time.sleep(COOLDOWN)
    leftclick()

    move_mouse(-595,0)
    for i in range(0,BLUE_ROCKET_SLOT):
        switch_weapon(5)
        time.sleep(COOLDOWN)
    time.sleep(4)
    dash()
    move_mouse(0,-675)
    time.sleep(COOLDOWN)
    leftclick()
    keyboard.press("space")
    time.sleep(COOLDOWN)
    keyboard.press_and_release("r")
    move_mouse(0,675)
    time.sleep(1)
    keyboard.release("space")
    hold_and_release_key("w",0.5)
    time.sleep(1.5)
    keyboard.press_and_release("control")
    time.sleep(LONG_COOLDOWN)
    #hold_and_release_key("control",0.5)
    keyboard.press("a")
    time.sleep(0.4)
    hold_and_release_key("control",0.58)
    keyboard.release("a")
    dashjump()
    time.sleep(0.85)
    hold_and_release_key("control",1.4)
    if HAS_HOTKEY_FOR_KNUCKLE_BLASTER:
        keyboard.press_and_release(KNUCKLE_BLASTER_HOTKEY) # assumes knuckle blaster is on G
    else:
        keyboard.press_and_release("f") # assumes knuckle blaster is pressed.
    time.sleep(COOLDOWN)
    reset_weapons()
    time.sleep(COOLDOWN)
    for i in range(0,RED_ROCKET_SLOT):
        switch_weapon(5)
        time.sleep(COOLDOWN)
    time.sleep(1)
    keyboard.press_and_release("control")
    time.sleep(0.5)
    #dash()
    move_mouse(-375,300)
    time.sleep(0.67) 
    keyboard.press("d")
    dash()
    time.sleep(0.01)
    keyboard.press("control")
    hold_rightclick(1.7)
    keyboard.release("control")
    keyboard.release("d")

#main
while True:
    if keyboard.is_pressed(HOTKEY):
        main_sequence()
    time.sleep(LONG_COOLDOWN)
