import os
import webbrowser
import pyautogui
from condition_checker import Condition
from time import sleep

condition = Condition()

# here i use webbrowser and pyautogui, because i have some issues with loading cookies and cache files in selenium, and also repeting login whatsapp
# maybe due to selenium and webdriver versions issues, i will update that in selenium later
# also pywhatkit does not properly working, some messages are not fully send
# and also sorry but this code can not run in pythonanywhere, i tested there, but in python anywhere, they didn't give permission to display the tab
# so if tab will not displayed then pyautogui can't work
# in selenium we can use --headless, so the script will run in background not in foreground.
# i will fix the issue with selenium, then i will update this code to selenium.

class SendMessage:

    def __init__(self):
        self.Trilochan_group_id = 'EZUzyUkyWcj1SiJ5Gh6PFD'
        self.py_id = 'JtohUjDiBPQ2oU2h0Dqt0z'
        self.dir_path = os.path.dirname(os.path.realpath(__file__))


    def send_meassages(self):
        condition.check()
        # for groups
        for i in condition.today_wishing_messages:
            webbrowser.open_new_tab(f"https://web.whatsapp.com/accept?code={self.Trilochan_group_id}")
            sleep(5)
            self.if_sleep()
            self.findtextbox()
            sleep(2)
            pyautogui.write(i['message'])
            sleep(3)
            pyautogui.press("enter")
            sleep(3)
            pyautogui.hotkey('ctrl', 'w')
        # for phone no
        for i in condition.today_wishing_messages:
            webbrowser.open_new_tab(f"https://web.whatsapp.com/send/?phone=91{i['phoneNo']}&text={i['message']}")
            sleep(35)
            self.if_sleep()
            pyautogui.press("enter")
            sleep(3)
            pyautogui.hotkey('ctrl', 'w')

    def findtextbox(self):
        """click on text box"""
        print('start')
        location = pyautogui.locateCenterOnScreen(f"{self.dir_path}\\data\\darktypemessage.png",confidence =0.6) 
        # if you faced an error :- NotImplementedError: The confidence keyword argument is only available if OpenCV is installed.
        # solution:- pip install opencv-python
        try:                                                                                                     
            pyautogui.moveTo(location[0] + 150, location[1] + 5)
            pyautogui.click()
            print("success")
        except Exception:
            location = pyautogui.locateCenterOnScreen(f"{self.dir_path}\\data\\whitetypemessage.png",confidence =0.6)
            pyautogui.moveTo(location[0] + 150, location[1] + 5)
            pyautogui.click()
            print("success")

    def if_sleep(self):
        try:
            print('check if_sleep')
            if pyautogui.locateCenterOnScreen(f"{self.dir_path}\\data\\whatsapp_endtoend.png",confidence =0.6):
                sleep(15)
                print('sleep for 15sec becz whatsapp still loaded')
            elif pyautogui.locateCenterOnScreen(f"{self.dir_path}\\data\\screeen_chat.png",confidence =0.6):
                sleep(15)
                print('sleep for 15sec becz still entering to group or phno chat')

        except pyautogui.ImageNotFoundException:
            print('pyautogui.ImageNotFoundException error found, skipped successfully')
            pass

run = SendMessage()
run.send_meassages()

# f'https://web.whatsapp.com/send/?phone=91{phoneNo}&text=message' send message to phone numbers
# https://web.whatsapp.com/accept?code=JtohUjDiBPQ2oU2h0Dqt0z  send message to groups
