import random
import time
print('\033[1;36mGAME CHALLENGE\033[m!')
print('MODE:\n'
      '\033[1;36m[ 1 ]\033[m - \033[1;32mCLASSIC\033[m\n'
      '\033[1;36m[ 2 ]\033[m - \033[1;35mCUSTOMIZED\033[m')
choice = int(input())
if choice == 1:
    pc = random.randint(1, 10)
    print('\033[1;36mThe computer will choose\033[m a number between \033[1;33m1 and 10\033[m\n'
          'And your chance for \033[1;32mwinning\033[m is \033[1;31m10%\033[m!\n'
          '\033[1;32mGood luck\033[m!')
elif choice == 2:
    s = int(input('Write the \033[32mstarting number\033[m: '))
    e = int(input('Write the \033[31mending number\033[m: '))
    print('The \033[1;36mcomputer will choose\033[m a number between \033[1;33m{} and {}\033[m\n'
          'And your chance for \033[1;32mwinning\033[m is \033[1;32m{:.2f}%\033[m!\n'
          '\033[1;32mGood luck\033[m!'
          .format(s, e, (1 /( (e-s) + 1 )*100)))
    pc = random.randint( s, e )
ct = 0 #COUNTER
print('For \033[1;31mQUIT\033[m type \033[1;35m2904\033[m')
user = int(input('\033[1;33mWrite your number\033[m: '))
while user != pc and user != 2904:
    print('\033[35mChecking...\033[m')
    time.sleep(0.5)
    print('\033[1;31mTry again!!\033[m')
    if user > pc:
        print('\033[1;40;31mLESS\033[m than \033[1;35m{}\033[m.'.format(user))
    else:
        print('\033[1;40;32mBIGGER\033[m than \033[1;35m{}\033[m.'.format(user))
    ct = ct + 1
    user = int(input('Write other guess: '))
if user == pc:
    print('You \033[1;32mwin\033[m!\n'
          'You \033[1;31mtried\033[m \033[1;35m{}\033[m times\n'
          'And the \033[1;4;40;34mnumber\033[m were \033[1;35m{}\033[m.'.format(ct+1, pc ))
else:
    print('\033[1;31mGAMEEEEEE OVERRRRRRRR\033[m\n'
          'You \033[1;31mtried\033[m \033[1;35m{} times\033[m and now is a \033[1;31mBIG BIG BIG\033[m \033[40;31mLOSER\033[m'.format(ct))
    print('And the \033[1;4;34;40mnumber\033[m were \033[1;35m{}\033[m'.format(pc))
