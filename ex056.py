print('\033[1;35mSome info\033[m \033[1;36mANALYSIS\033[m')
ct20 = 0 #COUNTER OF WOMAN THAT HAVE LESS 20 YEARS
mg = [] #MAN AGE
mn = [] #MAN NAME
ua = [] #USERS AGE
for c in range(1, 5):
    print('-----------PERSON {}----------'.format(c))
    name = str(input('Enter your \033[35mname\033[m: '))
    age = int(input('Enter your \033[34mage\033[m: '))
    ua.append(age)
    print('-----GENDER-----\n'
          '\033[1;36m[ FEMALE ]\033[m - 1\n'
          '\033[1;36m[ MALE ]\033[m - 2\n'
          '\033[1;36m[ OTHER ]\033[m - 3' )
    gender = int(input())
    if gender == 1:
        if age < 20:
            ct20 += 1 # OR ct20 = ct20 + 1
    if gender == 2:
        mg.append(age) # or sumage += age
        mn.append(name)
if mn  == []:
    print('There is \033[1;31mNo Man\033[m')
else:
    nman = mg.index(max(mg))
    print('The \033[1;36moldest man\033[m is {}'.format(mn[nman]))
print('The \033[1;33mAverage between\033[m all ages are {:.2f}'.format((ua[0] + ua[1] + ua[2] + ua[3]) / 4))
if ct20 >=1:
    print('{} \033[1;35mwoman\033[m has \033[1;31mless\033[m that \033[1;32m20 years old\033[m'.format(ct20))
else:
    print('There is \033[1;31mno woman\033[m that \033[1;35mhave less 20 years old\033[m')
