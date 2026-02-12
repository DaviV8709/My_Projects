print('\033[1;4;37;40mProducts and their prices\033[m')
import time
t = s = c =  0
ncheap = ''
pcheap = 0
#ncheap the cheapest product name
#pcheap price of the cheapest product
#t is a variable for products more than 1000
#s ACCUMULATOR
#c is a variable for total of products
while True:
    print(f'\033[1;35m.....................[ {c+1}º PRODUCT ].....................\033[m')
    name = str(input('\033[1;35mEnter\033[m the \033[1;33mproduct name\033[m: ')).capitalize()
    price = float(input('\033[1;35mEnter\033[m the \33[1;34mproduct price\033[m:R$ '))
    c = c + 1
    s = s + price
    if price > 1000:
        t = t + 1
    if c == 1:
        pcheap = price
        ncheap = name
    else:
        if price < pcheap:
            ncheap = name
    flag = ''
    while flag != 'Y' and flag != 'N':
        print('\033[40mMore products\033[m\n'
              '\033[1;32m[ Y ] - Yes\033[m\n'
              '\033[1;31m[ N ] - No\033[m')
        flag = str(input()).upper().strip()
    if flag == 'Y':
        print('\033[1;36mContinue...\033[m')
    elif flag == 'N':
        print('\033[1;35mAnalyzing....\033[m')
        time.sleep(1)
        break
    else:
        print('\033[1;31mInvalid option\033[m')
print('\033[1;34mSOME INFOS\033[m')
print(f'You entered \033[1;35m{c}\033[m \033[1;33mproducts and you will spend \033[m \033[1;35mR${s:.2f}\033[m with them')
print(f'There is/are \033[1;35m{t}\033[m \033[1;33mproducts at your list that are\033[m \033[1;35mmore than R$1,000.00\033[m')
print(f'The \033[1;32mcheapest product\033[m is \033[1;35m{ncheap}\033[m')
