import win32api, win32con, time,keyboard
def cooldown(seconds):
    time.sleep(seconds)
def leftclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    cooldown(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def rightclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    cooldown(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
def MoveMouse(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,x,y)

def SwitchWeapon(weapon:str):
    match weapon:
        case "1":
            PressAndRelease(weapon)
        case "2":
            PressAndRelease(weapon)
        case "3":
            PressAndRelease(weapon)
        case "4":
            PressAndRelease(weapon)
        case "5":
            PressAndRelease(weapon)

        case _:
            print(f"{weapon} is not a weapon choice")
    cooldown(0.01)
def PressAndRelease(key):
    keyboard.press_and_release(key)


def jump():
    PressAndRelease("space")
def walk(direction:str,seconds):
    keyboard.press(direction)
    cooldown(seconds)
    keyboard.release(direction)


def dash():
    PressAndRelease("shift")

def dashjump():
    dash()
    cooldown(0.01)
    jump()
    cooldown(0.01)
def slide(seconds):
    keyboard.press("control")
    cooldown(seconds)
    keyboard.release("control")
def reset_weapons():
    SwitchWeapon("1")
    SwitchWeapon("3")
    SwitchWeapon("2")
def main():
    reset_weapons()
    dashjump()
    cooldown(1.3)
    slide(0.5)
    MoveMouse(275,0)
    cooldown(0.1)
    slide(0.175)
    cooldown(0.2)
    MoveMouse(475,100)
    cooldown(0.75)
    #break pipe
    PressAndRelease("g")
    cooldown(0.75)
    walk("d",0.1)
    cooldown(0.01)
    slide(0.1)
    cooldown(0.05)
    MoveMouse(335,-100)
    cooldown(0.7)
    slide(0.8)
    cooldown(0.6)
    jump()
    cooldown(0.35)
    dash()
    cooldown(0.25)
    #outside
    MoveMouse(350,0)
    cooldown(0.7)
    slide(0.9)
    #nuke boost
    MoveMouse(-710,0)
    cooldown(0.1)
    jump()
    cooldown(0.1)
    rightclick()
    cooldown(0.01)
    MoveMouse(0,200)
    for i in range(0,2):
        SwitchWeapon("4")
    cooldown(0.01)
    leftclick()
    cooldown(0.01)
    MoveMouse(710,-200)
    SwitchWeapon("5")
    cooldown(3)
    dash()
    #MoveMouse(0,550)
    cooldown(0.05)
    keyboard.press("space")
    #dash()
    leftclick()
    cooldown(0.05)
    PressAndRelease("r")
    
    cooldown(0.5)
    keyboard.release("space")
    cooldown(1)
    keyboard.press("s")
    cooldown(0.5)
    keyboard.press("d")
    keyboard.release("s")
    cooldown(0.5)
    keyboard.release("d")
    PressAndRelease("space")
    cooldown(0.05)
    keyboard.press("d")
    cooldown(0.1)
    dash()
    cooldown(0.5)
    keyboard.release("d")
    cooldown(0.15)
    dashjump()
    cooldown(1)
    #cooldown(0.9)
    #slide(1)
    slide(3.2)
    #cooldown(0.01)
    #dash()
    #cooldown(0.5)
    #slide(3)
    leftclick()


    
    #MoveMouse(0,-550)


while True:
    if keyboard.is_pressed("t"):
        main()
        #break
    else:
        cooldown(0.01)