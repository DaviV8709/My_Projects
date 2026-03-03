print(f'{blue}Building and {purple}Analysing...{none}')
first = (f'{gray}[ 0,0 ]{none}', f'{gray}[ 0,1 ]{none}', f'{gray}[ 0,2 ]{none}')
second = (f'{gray}[ 1,0 ]{none}', f'{gray}[ 1,1 ]{none}', f'{gray}[ 1,2 ]{none}')
third = (f'{gray}[ 2,0 ]{none}', f'{gray}[ 2,1 ]{none}', f'{gray}[ 2,2 ]{none}')
l1 = []
l2 = []
l3 = []
whole = []
for c in range(1, 11):
    l1.append(int(input(f'{cyan}Enter a number{none} {first[c-1]} {red}(FIRST LINE){none}: '))) if c < 4 else ''
    l2.append(int(input(f'{cyan}Enter a number{none} {second[c-5]} {yellow}(SECOND LINE){none}: '))) if 4 < c < 8 else ''
    l3.append(int(input(f'{cyan}Enter a number{none} {third[c-8]} {green}(THIRD LINE){none}: '))) if 7 < c < 11 else ''
whole.append(l1)
whole.append(l2)
whole.append(l3)
three = 0
s = 0 #ACCUMULATOR
for part in whole:
    for num in part:
        three = three + 1
        print(f'{blue}[{none}  {purple}{num}{purple}  {blue}]{none}' , end= ' ')
        if three % 3 == 0:
            print('')
for number in whole:
    for n in number:
        if n % 2 == 0:
            s = s + n
print(f'The {red}SUM between {cyan}all EVEN NUMBERS is {purple}{s}{none}')
c3 = l1[2] + l2[2] + l3[2]
print(f'The {red}SUM between {green}all values on {blue}third colum is {purple}{c3}{none}')
print(f'The {red}Maximum value on {yellow}SECOND LINE is {purple}{max(l2)}{none}')
