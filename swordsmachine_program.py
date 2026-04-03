import win32con, win32api, time, keyboard,pyautogui

DEFAULTSECONDS = 0.001
def cooldown(seconds:float):
    time.sleep(seconds)

def Leftclick(seconds):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    cooldown(seconds)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def Rightclick(seconds):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    cooldown(seconds)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def MouseMove(x,y):
    win32api.mouse_event(win32con.MOUSE_MOVED,x,y)

def Slide(seconds):
    keyboard.press("control")
    cooldown(seconds)
    keyboard.release("control")
def Dash():
    keyboard.press_and_release("shift")
def Jump():
    keyboard.press_and_release("space")

def dashjump():
    Dash()
    cooldown(0.01)
    Jump()
def punch():
    keyboard.press_and_release("f")
def knuckleblast():
    keyboard.press_and_release("g")
def Walk(direction:str,seconds:float):
    direction = direction.lower()
    if direction == "w" or direction == "s" or direction == "a" or direction == "d":
        keyboard.press(direction)
        cooldown(seconds)
        keyboard.release(direction)
    else:
        print(f"Did you mean W or A or S or D instead of {direction}?")
def Swap_weapon(weapon_choice:str):
    weapon_choice = weapon_choice.lower()
    if weapon_choice == "1" or weapon_choice == "2" or weapon_choice == "3" or weapon_choice == "4" or weapon_choice == "5":
        keyboard.press_and_release(weapon_choice)
        cooldown(0.05)
    else:
        print(f"{weapon_choice} is not a weapon choice. May need to modify to include modded weapons")
def shotgunswapping(Max):
    for i in range(0,Max):
        keyboard.press_and_release("e")
        cooldown(0.5)
        Leftclick(0.1)
        #cooldown(0.01)
        knuckleblast()
        keyboard.press_and_release("q")
        cooldown(0.5)
        Leftclick(0.1)
def exitLevel():
    Slide(1.5)
    dashjump()
        


def SetDefault(): # makes sure shotgun is equipped
    pass
def main():
        Walk("w",1.5)
        dashjump()
        cooldown(1)
        MouseMove(0,-350)
        Rightclick(0.1)
        cooldown(0.1)
        for i in range(0,2):
            Swap_weapon("4")
        Leftclick(DEFAULTSECONDS)
        cooldown(0.55)
        knuckleblast()
        cooldown(0.5)
        MouseMove(-359,350) #-360 for x
        Slide(DEFAULTSECONDS)
        cooldown(0.3)
        Dash()
        cooldown(0.5)
        Walk("d",0.5)
        cooldown(DEFAULTSECONDS)
        Slide(2.8)
        cooldown(0.1)# in swords machine room
        Walk("w",0.5)
        Swap_weapon("3")
        Leftclick(2.3)
        keyboard.press_and_release("q")
        cooldown(0.5)
        Rightclick(0.01)
        cooldown(0.1)
        Swap_weapon("2")
        #swordsmachine spawn # time taken to spawn and first parry is ~1.75
        dashjump()
        cooldown(0.2)
        Walk("s",0.25)
        cooldown(1.27) 
        #punch()
        #punch()#parry swords machine
        Leftclick(0.1) #shotgun parry
        shotgunswapping(3) 
        cooldown(3)
        shotgunswapping(6)
        cooldown(1.5)
        exitLevel()


        #Dash()

while True:
    #pyautogui.displayMousePosition()
    if keyboard.is_pressed("]"):
        main()
        break