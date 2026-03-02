import time
print(f'\033[1;4;31;40mChallenge of ATM{none}')
n = int(input(f'{green}Enter a value{none}: '))
result = n
c50 = c20 = c10 = c5 = c1 = 0
bill50 = 50
bill20 = 20
bill10 = 10
bill5 = 5
bill1 = 1
while True:
    if result >= 50:
        result = result - bill50
        if result == 0:
            c50 = c50 + 1
            break
        elif result > 1:
            c50 = c50 + 1
    elif 50 > result >= 20:
        result = result - bill20
        if result == 0:
            c20 = c20 + 1
            break
        elif result > 1:
            c20 = c20 + 1
    elif 20 > result >= 10:
        result = result - bill10
        if result == 0:
            c10 = c10 + 1
            break
        elif result > 1:
            c10 = c10 + 1
    elif 10 > result >= 5:
        result = result - bill5
        if result == 0:
            c5 = c5 + 1
            break
        elif result > 1:
            c5 = c5 + 1
    elif result < 5:
        result = result - bill1
        if result == 0:
            c1 = c1 + 1
            break
        elif result > 0:
            c1 = c1 + 1
print(f'{purple}Counting....{none}')
time.sleep(1.5)
print(f'{gray}--------------------------------BILLS----------------------------{none}')
if c50 != 0:
    print(f'{purple}You{none} will {purple}get {c50}{none} bills of {purple}R$50,00{none}')
if c20 != 0:
    print(f'{red}You{none} will {red}get {c20}{none} bills of {red}R$20,00{none}')
if c10 != 0:
    print(f'{green}You{none} will {green}get {c10}{none} bills of {green}R$10,00{none}')
if c5 != 0:
    print(f'{yellow}You{none} will {yellow}get {c5}{none} bills of {yellow}R$5,00{none}')
if c1 != 0:
    print(f'{cyan}You{none} will {cyan}get {c1}{none} bills of {cyan}R$1,00{none}')
