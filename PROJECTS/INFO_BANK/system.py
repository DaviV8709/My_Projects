from lib.interface import *
from lib.archive import *
from time import sleep
arq = 'people.txt'
while True:
    choice = menu(['\033[34mSee all people entered\033[m', '\033[32mAdd other people\033[m', '\033[31mExit\033[m'])
    if choice == 1:
        title('\033[1;35m< PEOPLE ENTERED >\033[m', 50, '\033[1;35m')
        archiveRead(arq)
    elif choice == 2:
        x = list()
        register(x)
        data = f'{x[0]:^12}{x[1]:^15}{x[2]:^13}\n'
        archiveWrite(arq, data)
    elif choice == 3:
        title('\033[1;31;40mEXITING....\033[m', 50)
        sleep(2)
        break
    else:
        title('\033[31mYou entered an invalid option\033[m',50, '\033[31m')
        sleep(2)
