print('\033[1;35mFinding \033[1;33mEVENS \033[37m& \033[1;34mODDS\033[m')
numbers = []
while True:
    numbers.append(int(input('\033[1;37mEnter a number:\033[m ')))
    choice = ''
    print('\033[1;36mMore numbers: \033[1;32m[ Y ]\033[1;34m | \033[1;31m[ N ]\033[m')
    while choice != 'y' and choice != 'n':
        choice = str(input('')).lower()
        if choice not in 'yn':
            print('Enter a \033[1;4;31;40mvalid option\033[m')
    if choice == 'n':
        break
even = []
odd = []
for number in numbers:
    even.append(number) if number % 2 == 0 else odd.append(number)
print('\033[1;36mYou entered {}'.format(numbers))
print(f'\033[1;33mEVEN numbers:\033[m \033[33m{even}\033[m' if even != [] else 'There \033[1;31mare no\033[m \033[33mEVEN numbers\033[m')
print(f'\033[1;34mODD numbers:\033[m \033[34m{odd}\033[m' if odd != [] else 'There \033[1;31mare no\033[m \033[34mODD numbers\033[m')
