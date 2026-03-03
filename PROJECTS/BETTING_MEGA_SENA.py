print( '\033[1;34m-*\033[m' * 10 ,f'{"\033[1;33mMEGA \033[1;34mSENA \033[1;33mChallenge":^30}', '\033[1;34m-*\033[m' * 10)
from random import randint
from time import sleep
bet = []
game = []
ct = 0
order = ('\033[31mFIRST\033[m', '\033[32mSECOND\033[m', '\033[33mTHIRD\033[m', '\033[34mFOURTH\033[m', '\033[35mFIFTH\033[m', '\033[36mSEVENTH\033[m', '\033[37mEIGHTH\033[m')

amount = int(input('\033[1;35mHow many games: \033[m'))
for games in range(0, amount ):
    for c in range(0, 6):
        pc = randint(1, 60)
        if pc not in game:
            game.append(pc)
        else:
            pc = randint(1, 60)
            game.append(pc)
    bet.append(game[:])
    game.clear()
print(f'\033[33mThe program will show will \033[1;32m[ {amount} ]\033[m \033[35mpossibilities of betting bellow\033[m: ')
print('>>>'*20)
for bets in bet:
    sleep(1)
    print(f'The {order[ct]} \033[40mbet\033[m is {bets}' if amount <=8 else f'\033[1;34m[ {ct+1}ª ]\033[m GAME: \033[1;37m{bets}\033[m')
    ct = ct + 1
print(f'{"\033[1;32mGOOD LUCK!\033[m":^60}')
print('>>>'*20)
