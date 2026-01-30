print('\033[4;40mUnit converter\033[m')
red = '\033[1;31m'
green = '\033[1;32m'
blue = '\033[1;34m'
purple = '\033[1;35m'
yellow = '\033[1;33m'
lblue = '\033[1;36m'
gray = '\033[1;37m'
none = '\033[m'
print('{}1{} for convert to {}binary{}\n'
      '{}2{} for convert to {}octal{}\n'
      '{}3{} for convert to {}hexadecimal{}'
      .format(red , none, red, none, blue, none, blue, none, green, none, green, none))
choice = int(input('Enter conversor: '))
number = int(input('Enter a number: '))
if choice == 1:
    print('The decimal number {} in {}binary{} is {}'.format(number, red, none, bin(number)[2:]))
elif choice == 2:
    print('The decimal number {} in {}octal{} is {}'.format(number, blue, none, oct(number)[2:]))
else:
    print('The decimal {} in {}hexadecimal{} is {}'.format(number, green, none, hex(number)[2:]))
