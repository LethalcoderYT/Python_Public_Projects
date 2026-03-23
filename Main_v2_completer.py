#note you have to have marksman revolver pre-equipped
import win32api, win32con, time, keyboard

Running = True
COOLDOWN = 0.1
MAX = 6
def cooldown():
    time.sleep(COOLDOWN)
def cooldown_with_params(num):
    time.sleep(num)

def leftclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    cooldown_with_params(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

def rightclick():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN,0,0)
    cooldown_with_params(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP,0,0)

def move_mouse(x:int,y:int):
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE,x,y)

def dash_jump():
    keyboard.press("shift")
    cooldown_with_params(0.05)
    keyboard.press("space")
    cooldown()
    keyboard.release("shift")
    keyboard.release("space")
    cooldown_with_params(0.7)
def jump():
    keyboard.press_and_release("space")
def whiplash():
    keyboard.press_and_release("r")
def punch():
    keyboard.press_and_release("f")
def dash():
    keyboard.press_and_release("shift")

def walk(direction:str,ammount_of_time:float):
    key = ""
    match direction:
        #w for forward
        #s for backward
        #a for left
        #d for right
        case "w":
            key = "w"

        case "s":
            key = "s"

        case "a":
            key = "a"

        case "d":
            key ="d"
        case _:
            print(f"problem occured {direction} doesn't exist ")

    keyboard.press(key)
    cooldown_with_params(ammount_of_time)
    keyboard.release(key)
    
def slide(ammount_of_time:float):
    keyboard.press("control")
    cooldown_with_params(ammount_of_time)
    keyboard.release("control")
def bunnyhop():
    #cooldown()
    slide(0.02)
    jump()
    #slide(0.1)
    #cooldown()
def coinpunching():
    Max = 5
    jump()
    move_mouse(0,350)
    cooldown()
    rightclick()
    cooldown_with_params(0.45)
    punch()
    move_mouse(0,-350)
    cooldown_with_params(0.45)
    punch()
    for i in range (0,Max):
        slide(0.001)
        cooldown_with_params(0.35)
        jump()
        cooldown_with_params(0.45)
        punch()

        


#FINAL PRODUCT
def main():
    global Running
    while True:
        if Running:
            #main speedrunning part
            if keyboard.is_pressed("]"):
                walk("w",1)
                slide(1)
                cooldown()
                dash_jump()
                cooldown_with_params(0.55)
                #bunnyhop
                for i in range(0,MAX):
                    #print(i)
                    bunnyhop()
                    if i !=MAX-1:
                        cooldown_with_params(1.2)
                    else:
                        cooldown_with_params(0.3)
                    #slide(0.1)
                #slide(0.05)
                jump()
                cooldown_with_params(0.3)
                #jump()
                move_mouse(0,-70)
                cooldown_with_params(0.01)
                whiplash()
                cooldown_with_params(0.01)
                #dash()
                move_mouse(0,70)
                cooldown_with_params(1)
                for i in range(0,2):
                    jump()
                    cooldown_with_params(0.1)
                    slide(0.0001)
                    cooldown_with_params(0.1)
                    jump()
                    cooldown_with_params(0.1)
                cooldown_with_params(1)
                dash()
                cooldown_with_params(0.5)
                #dash()
                #cooldown_with_params(1.5)
                #slide(0.001)
                cooldown_with_params(1)
                slide(2.9)
                #v2 boss fight triggered
                cooldown_with_params(1.1)
                slide(0.001)
                cooldown_with_params(0.3)
                coinpunching()
                cooldown_with_params(2)
                
                walk("s",2)
                slide(4.3)
                dash()
                cooldown_with_params(0.5)
                leftclick()


                #dash()


                Running = False

            #exiting
            elif keyboard.is_pressed("["):
                Running = False
            else:
                cooldown()
                
        else:
            break
main()
#while True:
#    if keyboard.is_pressed("]"):
#        coinpunching()
#        break