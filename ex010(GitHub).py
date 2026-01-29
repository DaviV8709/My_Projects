print('Welcome to the conversor BRL to USD and EUR')
w=float(input('How much do you have in your wallet \033[1;32min R$\033[m: '))

print('\033[31mATTENTION CHECK ON THE INTERNET\033[m')

pd=float(input('What is the exchange now \033[1;34mBRL to USD: \033[m'))
pe=float(input('What is the exchange now \033[1;33mBRL to EUR: \033[m'))
d=w/pd
e=w/pe
yellow = '\033[1;33m'
blue = '\033[1;34m'
green = '\033[1;32m'
none = '\033[m'
print('You can buy {}U${:.2f}{} with {}R${:.2f}{}, '
      'considering the price of {}R${:.2f}{}'.format(blue,d,none,green,w,none,green,pd,none))
print('You can buy {}€{:.2f}{} with {}R${:.2f}{}, '
      'considering the price of {}R${:.2f}{}'.format(yellow,e,none,green,w,none,green,pe,none))