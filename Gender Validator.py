print('Challenge of validating')
gender = ''
print('[ M ] - Male\n'
      '[ F ] - Female\n'
      '[ O ] - Other')
while gender != 'F' and gender != 'M' and gender != 'O':
    gender = str(input('Enter your \033[1;32mgender\033[m: ')).strip().upper()
    if gender != 'F' and gender != 'M' and gender != 'O':
        print('\033[1;31mOption not accepted\033[m\n'
              '\033[1;32mTry again!\033[m')
if gender == 'F':
    print('Your \033[1;36mgender\033[m is \033[1;34mFemale\033[m')
elif gender == 'M':
    print('Your \033[1;36mgender\033[m is \033[1;34mMale\033[m')
else:
    gender2 = str(input('Write your \033[1;33mgender\033[m: '))
    print('Your {}gender{} is \033[1;34m{}\033[m'.format('\033[1;36m', '\033[m',gender2))
