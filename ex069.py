print('\033[1;35mReading some infos!\033[m')
import time
p = p18 = w20 = m = 0
sex = ''
choice = ''
line = 'FIRST' , 'SECOND', 'THIRD', 'FOURTH', 'FIFTH', 'SIXTH', 'SEVENTH', 'EIGHTH', 'NINTH'
#p is a variable for the total of people entered
#p18 is a variable for the total of people that have more than 18
#w20 is a variable for the total of women that have less than 20
#m is a variable for the total of men
while True:
    print(f'---------------\033[1;35m{line[p]} PERSON\033[m --------------------')
    age = int(input('\033[1;33mEnter\033[m your \033[1;33mage\033[m: '))
    if age > 18:
        p18 = p18 + 1
    while sex != 'M' and sex != 'F' and sex != 'O':
        print('\033[1;36m[ M ]\033[m - Male\n'
              '\033[1;36m[ F ]\033[m - Female\n'
              '\033[1;36m[ O ]\033[m - Other')
        sex = str(input()).upper().strip()
    if sex == 'M':
        m = m + 1
    if sex == 'F':
        if age < 20:
            w20 = w20 + 1
    if sex == 'O':
        other = str(input('\033[1;35mWrite\033[m your \033[1;36mgender\033[m: '))
        print(f'Your \033[1;36mgender\033[m is \033[1;36m{sex}\033[m')
    p = p + 1
    while choice != 'Y' and choice != 'N':
        print('\033[1;37mMore people\033[m\n'
             '\033[1;32m[ Y ]\033[m - \033[32mYes\033[m\n'
             '\033[1;31m[ N ]\033[m - \033[31mNo\033[m')
        choice = str(input()).upper().strip()
    if choice == 'Y':
        print('\033[36m=-\033[m' * 20)
        print('\033[1;36mNext person\033[m')
        print('\033[36m=-\033[m' * 20)
        time.sleep(1)
        choice = ''
        sex = ''
    elif choice == 'N':
        print('\033[31m=-\033[m' * 20)
        print('\033[1;31mClosing...\033[m')
        print('\033[31m=-\033[m' * 20)
        time.sleep(1.5)
        break
    else:
        print('Enter a \033[1;31mvalid option\033[m')
print('\033[1;35m------------------------------INFOS-------------------------\033[m')
print(f'\033[1;34mPeople entered:\033[m \033[1;35m{p}\033[m')
print(f'\033[1;32mWomen that have less\033[m 20 years old: \033[1;35m{w20}\033[m')
print(f'\033[1;36mMan entered\033[m: \033[1;35m{m}\033[m')
print(f'\033[1;31mPeople that have less\033[m than 18 years: \033[1;35m{p18}\033[m')
