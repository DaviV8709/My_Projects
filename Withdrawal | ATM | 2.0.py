b2 = b5 = b10 = b20 = b50 = b100 = b200 = 0
print('\033[1;31m[ ATM ]\033[m by \033[4;31;40m[ Davi Vicente ]\033[m')
n = int(input('\033[1;32mEnter a value\033[m:R$ '))
result = n
while True:
    if result >= 200:
        result = result - 200
        if result > 0:
            b200 = b200 + 1
        elif result == 0:
            b200 = b200 + 1
            break
    if result < 200 and result >= 100:
        result = result - 100
        if result > 0:
            b100 = b100 + 1
        elif result == 0:
            b100 = b100 + 1
            break
    if result < 100 and result >= 50:
        result = result - 50
        if result > 0:
            b50 = b50 + 1
        elif result == 0:
            b50 = b50 + 1
            break
    if result < 50 and result >= 20:
        result = result - 20
        if result > 0:
            b20 = b20 + 1
        elif result == 0:
            b20 = b20 + 1
            break
    if result < 20 and result >= 10:
        result = result - 10
        if result > 0:
            b10 = b10 + 1
        elif result == 0:
            b10 = b10 + 1
            break
    if result < 10 and result >= 5:
        result = result - 5
        if result > 0:
            b5 = b5 + 1
        elif result == 0:
            b5 = b5 + 1
            break
    if result < 5 and result >= 2:
        result = result - 2
        if result > 0:
            b2 = b2 + 1
        elif result == 0:
            b2 = b2 + 1
            break
    if result < 2:
        print(f'\033[1;334mWe are going\033[m to get \033[1;32mR${result}\033[m for \033[31mtaxes and interest\033[m')
        print('\033[1;33mJust Kidding!\033[m')
        sp = result
        break
print(f'\033[1;32mR${n:.2f}\033[m can be \033[1;34mwithdrawn with\033[m \033[1;35m{b200+b100+b50+b20+b10+b5+b2} bills\033[m:')
#print(f'\033[1;35mLEFTOVER\033[m:\033[42m[ {sp} ]\033[m')
if b200 != 0:
    print(f'\033[1;31m{b200}\033[m bills of \033[1;31mR$200.00\033[m \033[4;31m[ TOTAL ]\033[m \033[1;31mR${b200*200:.2f}\033[m')
if b100 != 0:
    print(f'\033[1;32m{b100}\033[m bills of \033[1;32mR$100.00\033[m \033[4;32m[ TOTAL ]\033[m \033[1;32mR${b100 * 100:.2f}\033[m')
if b50 != 0:
    print(f'\033[1;33m{b50}\033[m bills of \033[1;33mR$50.00\033[m \033[4;33m[ TOTAL ]\033[m \033[1;33mR${b50 * 50:.2f}\033[m')
if b20 != 0:
    print(f'\033[1;34m{b20}\033[m bills of \033[1;34mR$20.00\033[m \033[4;34m[ TOTAL ]\033[m \033[1;34mR${b20*20:.2f}\033[m')
if b10 != 0:
    print(f'\033[1;35m{b10}\033[m bills of \033[1;35mR$10.00\033[m \033[4;35m[ TOTAL ]\033[m \033[1;35mR${b10*10:.2f}\033[m')
if b5 != 0:
    print(f'\033[1;36m{b5}\033[m bills of \033[1;36mR$5.00\033[m \033[4;36m[ TOTAL ]\033[m \033[1;36mR${b5*5:.2f}\033[m')
if b2 != 0:

    print(f'\033[1;37m{b2}\033[m bills of \033[1;37mR$2.00\033[m \033[4;37m[ TOTAL ]\033[m \033[1;37mR${b2*2:.2f}\033[m')
