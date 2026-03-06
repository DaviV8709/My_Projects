
def line(tam = 40):
    print('='*tam)


def readint(msg):
    while True:
        try:
            num = int(input(msg))
        except KeyboardInterrupt:
            break
        except:
            print('\033[31mYou entered an invalid number\033[m')
            continue
        else:
            return num


def title(txt, position = 42, color = '\033[38m'):
    print(f'{color}=\033[m'*41)
    print(f'{txt:^{position}}')
    print(f'{color}=\033[m'*41)


def menu(list):
    title('\033[1;36m MENU\033[m', 50, '\033[1;36m')
    line()
    for number, item in enumerate(list):
        print(f'{item:.<42}\033[1;37m[ {number+1} ]\033[m')
    line()
    x = readint('\033[1;34mSelect a option:\033[m \n')
    return x


def register(list):
    title('\033[1;38mADDING PEOPLE\033[m',50)
    list.append(str(input('\033[34mEnter your name:\033[m ')))
    list.append(int(input('\033[33mEnter your age:\033[m ')))
    gender = (str(input('\033[35mEnter your gender\033[m\n'
                            '\033[1;36m[ F ] - \033[1;38mFEMALE\033[m\n'
                            '\033[1;36m[ M ] - \033[1;38mMALE\n'
                            '\033[1;36m[ O ] - \033[1;38mOTHER\n'))).upper()
    while gender not in 'MFO':
        gender = str(input('\033[1;31mYou entered an invalid option\n'
                           'Try again:\033[m ')).upper()
    if gender == 'O':
        list.append(str(input('\033[1;36mWrite your gender: \033[m')))
    elif gender == 'F':
        list.append('FEMALE')
    else:
        list.append('MALE')
