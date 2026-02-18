print('\033[1;35mPutting some numbers at one list\033[m')
numbers = []
while True:
    numbers.append(int(input('\033[1;33mEnter a number:\033[m ')))
    print('\033[1;36mMore number: \033[32m[ Y ] \033[34m/ \033[31m[ N ]\033[m')
    choice = str(input())
    while choice not in 'YyNn':
        print('\033[1;31mINVALID OPTION\033[m')
        choice = str(input('\033[1;34mEnter \033[1;33mit a again: \033[m'))
    if choice in 'Nn':
        break
print(f'You \033[1;35mentered \033[32m[ {len(numbers)} ] numbers\033[m')
print(f'\033[1;35mYour numbers in a \033[37m| DESCENDING ORDER |\033[m\n'
      f'\033[1;34m{sorted(numbers, reverse=True)}\033[m')
print('You' , '\033[1;31mdo not\033[m entered \033[1;32mnumber five\033[m' if not 5 in numbers else '\033[1;33mentered the \033[1;32mnumber five\033[m')
