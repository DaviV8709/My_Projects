import time
choice = 0
print('\033[1;31mWelcome to the math Menu!\033[m\n'
      '\033[36mFirst of all\033[m enter \033[33mtwo numbers\033[m')
n1 = int(input('Enter the \033[32mfirst number\033[m: '))
n2 = int(input('Enter the \033[34msecond number\033[m: '))
print(    '\033[1;36m[ 1 ]\033[m \033[1;31mSum\033[m \033[1;33m{}\033[m and \033[1;34m{}\033[m\n'
          '\033[1;36m[ 2 ]\033[m \033[1;32mMultiply\033[m \033[1;33m{}\033[m and \033[1;34m{}\033[m\n'
          '\033[1;36m[ 3 ]\033[m \033[1;33mBigger between\033[m \033[1;33m{}\033[m and \033[1;34m{}\033[m\n'
          '\033[1;36m[ 4 ]\033[m \033[1;34mNew numbers\033[m\n'
          '\033[1;36m[ 5 ]\033[m \033[1;35mExit\033[m\n'
          .format(n1, n2, n1, n2, n1, n2))
while choice == 0:
    print('\033[37mWhat do you want to do?\033[m')
    choice = int(input())
    if choice == 1:
        result = n1 + n2 #THE PRINT COULD be here
        choice = 1
    elif choice == 2:
        result = n1 * n2 # YOU MADE A IF TWICE WITHOUT NEED!!!!!
        choice = 2
    elif choice == 3: # DONT DO IT AGAIN.
        choice = 3
    elif choice == 4:
        choice = 0
        n1 = int(input('Enter the new \033[32mfirst number\033[m: '))
        n2 = int(input('Enter the new \033[34msecond number\033[m: '))
        print('\033[1;36m[ 1 ]\033[m \033[1;31mSum\033[m \033[1;33m{}\033[m and \033[1;34m{}\033[m\n'
              '\033[1;36m[ 2 ]\033[m \033[1;32mMultiply\033[m \033[1;33m{}\033[m and \033[1;34m{}\033[m\n'
              '\033[1;36m[ 3 ]\033[m \033[1;33mBigger between\033[m \033[1;33m{}\033[m and \033[1;34m{}\033[m\n'
              '\033[1;36m[ 4 ]\033[m \033[1;34mNew numbers\033[m\n'
              '\033[1;36m[ 5 ]\033[m \033[1;35mExit\033[m\n'
              .format(n1, n2, n1, n2, n1, n2))
    elif choice == 5:
        choice = 'EXIT'
    else:
        print('\033[31mSelect a valid option\033[m\n'
              '\033[37mAnd try again\033[m')
        choice = 0
if choice == 'EXIT':
    print('\033[36mClosing...\033[m')
    time.sleep(1.5)
    print('\033[35mThanks for using\033[m.\n'
          '\033[34mSee you next time\033[m!')
elif choice == 1:
    print('The \033[31;40mSUM\033[m between \033[1;33m{}\033[m and \033[1;34m{}\033[m is \033[1;35m{}\033[m'.format(n1, n2, result))
elif choice == 2:
    print('The \033[32;40mMULTIPLY\033[m between \033[1;33m{}\033[m and \033[1;34m{}\033[m is \033[1;35m{}\033[m'.format(n1, n2, result))
elif choice == 3:
    if n1 > n2:
        result = n1
        print('\033[1;33m{}\033[m is \033[33;40mBIGGER THAN\033[m \033[1;34m{}\033[m'.format(n1, n2 ))
    elif n2 > n1:
        print('\033[1;34m{}\033[m is \033[33;40mBIGGER THAN\033[m \033[1;33m{}\033[m'.format(n2, n1 ))
    else:
        print('\033[34mThey are equal!\033[m')
