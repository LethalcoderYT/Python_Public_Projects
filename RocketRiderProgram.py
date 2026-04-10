import win32api, win32con, keyboard, time


def cooldown(amount_of_time:float):
    time.sleep(amount_of_time)
def leftclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    cooldown(0.25)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
def rightclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    cooldown(0.25)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)
def MoveMouse(x,y):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,x,y)
def whiplash():
    keyboard.press_and_release("r")
def Weapon_switching(switch_to:str):
    match switch_to:
        case "1":
            keyboard.press_and_release(switch_to)
        case "2":
            keyboard.press_and_release(switch_to)
        case "3":
            keyboard.press_and_release(switch_to)
        case "4":
            keyboard.press_and_release(switch_to)
        case "5":
            keyboard.press_and_release(switch_to)
        case "e":
            keyboard.press_and_release(switch_to)
        case "q":
            keyboard.press_and_release(switch_to)
        case _:
            print(f"{switch_to} isn't a weapon slot pls modify if it includes mods")
    cooldown(0.1)

    
def main():
    #resets weapon to be 100% sure
    Weapon_switching("1")
    Weapon_switching("2")

    Weapon_switching("5")
    MoveMouse(0,350)
    cooldown(0.05)
    leftclick()
    cooldown(0.05)
    whiplash()
    cooldown(0.05)
    MoveMouse(0,-350)
    keyboard.press("s")
    cooldown(0.5)
    keyboard.release("s")


while True:
    if keyboard.is_pressed("t"):
        main()
    else:
        cooldown(0.001)
