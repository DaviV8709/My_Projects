print('[ \033[1;33mChallenge of multiplication table\033[m ]')
n = float(input('Enter a \033[1;32mnumber\033[m: '))
for c in range(1,11):
    print('\033[34m{}\033[m X \033[31m{}\033[m = \033[36m{}\033[m'.format(n, c, n*c ))
