print('\033[1;4;33mChallenge of prime numbers\033[m')
n = int(input('Enter a \033[36mnumber\033[m: '))
ct = 0
for c in range(1, n +1):
    if n % c == 0:
        print('\033[34m', c, '\033[m' , end ='-')
        ct = ct + 1
    else:
        print('\033[31m', c, '\033[m', end ='-')
print(' ')
print('\033[35m{}\033[m were \033[34mdivided\033[m \033[1;34m{}\033[m times\nAnd \033[35mbecause\033[m of it:'
      .format(n ,ct))
if ct == 2:
    print('\033[35m[ {} ]\033[m \033[32mIts a prime number\033[m'.format(n))
else:
    print('\033[35m[ {} ]\033[m \033[31mIts not a prime number\033[m'.format(n))
