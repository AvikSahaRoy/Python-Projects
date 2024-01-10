# Search - pywhatkit
# Install - pip install pywhatkit
import pywhatkit
import pyautogui
# import time
i = 1
pywhatkit.sendwhatmsg('+917363009328', 'Hii Gopal', 22, 5)
while i<=5:
    # time.sleep(0)
    pyautogui.typewrite('Good AfterNoon')
    pyautogui.press('enter')
    i += 1



# # ==============================================================

# #Whatsapp Bot
# import pywhatkit
# from datetime import datetime
# import pyautogui

# now = datetime.now()

# c = now.strftime("%H")
# mobile = input('Enter Mobile No of Receiver: ')
# message = input('Enter Message you wanna send: ')
# many=int(input("How Many Time: "))
# hour = int(input('Enter hour: '))
# minute = int(input('Enter minute: '))

# i = 1
# pywhatkit.sendwhatmsg(mobile, message, hour, minute)
# while i<many:
#     pyautogui.typewrite(message)
#     pyautogui.press('enter')
#     i += 1

