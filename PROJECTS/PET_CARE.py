purple = '\033[1;35m'
white = '\033[1;38m'
none = '\033[m'
red = '\033[1;31m'
print(f'{white}Welcome to the {purple}PET CARE SYSTEM!{none}')
process = (f'{purple}FIRST{none}', f'{white}SECOND{none}', f'{purple}THIRD{none}', f'{white}FOURTH{none}', f'{purple}FIFTH{none}')
#info = [{'Name': 'Catarina' , 'Specie': 'Cat', 'Persona': 'Calm', 'Human': 'Solange', 'Cares': 3, 'Actions': ['Bath']}] # TESTS
info = list()
pet = dict()
action = list()
while True:
    pet['Name'] = str(input(f'\033[1;38mEnter the \033[31mpets name:{none} ')).capitalize().strip()
    pet['Specie'] = str(input(f'\033[1;38mEnter the \033[31mpets specie:{none} ')).capitalize().strip()
    pet['Persona'] = str(input(f'\033[1;38mEnter the \033[31mpets personality:{none} ')).capitalize().strip()
    pet['Human'] = str(input(f'\033[1;38mEnter the \033[31mpets human name:{none} ')).capitalize().strip()
    print(f'\033[4;38mHow many process:{none}')
    pet['Cares'] = int(input())
    for c in range(0, pet['Cares']):
        action.append(str(input(f'Enter the {process[c]} process: ' if pet['Cares'] < 6 else f'{white}Enter the {purple}{c+1}{none}ª process: ')).capitalize())
    pet['Actions'] = action[:]
    print(f'\033[1;35;40mNOTE{none}\n'
          f'\033[32m[ YES ] \033[1;31m[ NO ]{none}')
    note = str(input())[0].upper()
    if note == 'Y':
        pet['Note'] = str(input(f'{purple}Enter a note: {none}')).upper().strip()
    info.append(pet.copy())
    action.clear()
    print(f'\033[31mMORE PETS: {purple}[ Y ] {white}| [ N ]{none}')
    more = str(input())[0].upper()
    while more not in 'YN':
        print(f'\033[1;31mYou entered an invalid option{none}')
        more = str(input())[0].upper()
    if more == 'N':
        break
    print(f'\033[1;35;40mNEXT PET.....{none}')
choice = ''
while True:
    if choice == 'E':
        break
    print(f'{purple}   [ NAME ]      [ CARES ]     [ HUMAN ]     [ PRIORITY ]{none}')
    for pet in info:
        print(f'{pet['Name']:^15}{pet['Cares']:^13}\033[1;37m{pet['Human']:^15}{none}{f'{"\033[1;31mURGENT\033[m":^28}' 
        if pet['Cares'] > 5 else f'{"\033[1;33mBE ATTENTION\033[m":^28}' 
        if 5 >= pet['Cares'] >= 3 else f'{"\033[1;32mNOTICE\033[m":^28}'}')
    print(f'{purple}MORE INFO: \033[32m[ YES ] \033[31m[ NO ]{none}')
    extra = str(input())[0].upper()
    while extra != 'N' and extra != 'Y':
        print(f'\033[1;31mYou entered an invalid option{none}\n'
              f'{purple}Enter it again: {none}')
        extra = str(input())[0].upper()
    if extra == 'N':
        break
    elif extra == 'Y':
        choice = 'again'
        while choice == 'again':
            print(f'{white}Enter the \033[31mname of the pet:{none} ')
            name = str(input().capitalize())
            ct = len(info)
            for pet in info:
                if pet['Name'] == name:
                   print(f'All about {name}')
                   for key, value in pet.items():
                       print(f'{purple}[ {key} ]{none} : \033[38m[ {value} ]{none}')
                   print(f'\033[1;38mVIEW other pets Data{none}\n'
                         f'\033[1;32m[ YES ] \033[1;31m[ EXIT ] \033[1;37m[ LIST ]{none}')
                   choice = str(input())[0].upper()
                else:
                    ct = ct -1
                    if ct == 0:
                        print(f'\033[38mYou entered an \033[31;40minvalid option{none} '
                              f'{white}[ {name} ] \033[31mis not at the \033[1;35mlist{none}')
                        choice = 'again'
            if choice == 'E':
                choice = 'E'
            elif choice == 'Y':
                choice = 'again'
            elif choice == 'L':
                choice = ''
print('\033[32mThanks for Using\033[m\n'
      '\033[38mDeveloped by \033[1;4;32;40mDavi S.\033[m')
