print('\033[1;36mGAME\033[m - \033[33mEvens\033[m and \033[34mOdds\033[m')
player = ''
w = 0
#w is a variable for user winnings
import random
import time
while True:
    while player != 'EVEN' and player != 'ODD':
        print('\033[1;33m[ EVEN ]\033[m \033[1;34m[ ODD ]\033[m')
        player = str(input()).upper().strip()
        if player == 'EVEN':
            user = 0
            pc = 1
        elif player == 'ODD':
            user = 1
            pc = 0
        else:
            print('\033[1;35mEnter\033[m a \033[1;31mvalid option\033[m')
    print('-'*40)
    item = ('\033[1;33mEVEN\033[m', '\033[1;34mODD\033[m')
    n1 = int(input('\033[1;36mEnter your number\033[m: '))
    if n1 > 5:
        print('\033[1;31mImpossible to make this\033[m number with \033[1;36myour fingers!\033[m')
    n2 = random.randint(0,5)
    game = (n1 + n2) % 2
    if game == user:
        print('\033[1;4;32;40mVICTORY!\033[m\n'
              f'\033[1;36mYou chose\033[m {n1}\n'
              f'\033[1;34mPC chose\033[m {n2}\n'
              f'\033[1;35mSUM\033[m: {n1+n2} | \033[40;mWINNER\033[m: {item[game]}')
        player = ''
        w = w + 1
    elif game == pc:
        break
print('\033[1;4;31;40mGAME OVER!\033[m\n'
              f'\033[1;31mYou chose\033[m {n1}\n'
              f'\033[1;32mPC chose\033[m {n2}\n'
              f'\033[1;35mSUM\033[m: {n1+n2} | \033[40;mWINNER\033[m: {item[game]}')
print(f'You \033[1;31mwon:\033[m\n'
      f'\033[1;35m[ {w} ] in a ROW\033[m ')
