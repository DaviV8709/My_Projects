print('Temperature convertor')
print('\033[4;1;31mFYI: 1C° is equivalent to 33.8F°\033[m')
c=float(input('Put the temperature \033[4;34min Celsius\033[m: '))
print('The actual temperature in \033[4;33mFahrenheit\033[m is \033[33m{:.1f}Fº\033[m'.format( ( (c*9/5) + 32) ) )