import datetime
import time
import pyautogui


#Input part
while True:
    try:
        i = int(input("How many times u want messages to be sent?"))
        if(i>0):
            break
        else:
            raise Exception("U need to type number bigger than 0")    
    except: print("Try again")
    
check = i
#Spam part
while i!=0:

    if(i == check):
        time.sleep(7) #U have 7 seconds to click on open app u wanna use if u need more replace 7 with something else.
    else:   
        time.sleep(1)    

    print(datetime.datetime.now())
    pyautogui.typewrite("cool")
    pyautogui.press("enter")
    time.sleep(1)

    print(datetime.datetime.now())
    pyautogui.typewrite("this is god of sun(RA)") #If u want to send link paste it between " ".
    pyautogui.press("enter")
    time.sleep(1)

    print(datetime.datetime.now())
    pyautogui.typewrite("easyy")
    pyautogui.press("enter")
    time.sleep(1)

    print(datetime.datetime.now())
    pyautogui.typewrite("hi")
    pyautogui.press("enter")
    time.sleep(1)

    print(datetime.datetime.now())
    pyautogui.typewrite("Winner winner chicken dinner")
    pyautogui.press("enter")
    time.sleep(1)

    print(datetime.datetime.now())
    pyautogui.typewrite("who are u")
    pyautogui.press("enter")
    time.sleep(1)

    i=i-1

print("Script is done.")