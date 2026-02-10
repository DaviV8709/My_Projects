print('Challenge of reading numbers 2')
ac = 0 #ACCUMULATOR
ct = 0 #COUNTER
bigger = 0
smaller = 0
numbers = []
choice = ''
while choice != 'N':
    n = int(input('Enter a number: '))
    print('Continue: [ Y ] / [ N ]')
    choice = str(input()).upper()
    if choice != 'N' and choice != 'Y':
        print('This option is not available')
    else:
        ac = ac + n
        ct = ct + 1
        if ct == 1:
            bigger = smaller = n
        else:
            if n > bigger:
                bigger = n
            if n < smaller:
                smaller = n
    numbers.append(n)
print('The Average between all {} numbers entered is {:.2f}'
      .format(ct, ac/ct))
print('=*'*50)
print('\033[1;35mTHE BIGGEST AND THE SMALLEST VALUE\033[m')
print('=*'*50)
print('-'*100)
print('\033[1;34mUsing the LIST\033[m - |max| and |min|')
print('-'*100)
print('The max value entered were: {}\n'
      'The min value entered were: {}'
      .format(max(numbers), min(numbers)))
print('numbers.append(n)\n'
      'max(n)\n'
      'min(n)')
print('-'*100)
print('\033[1;31mUsing mathematics\033[m')
print('-'*100)
print('The biggest value was: {}\n'
      'The smallest value was: {}'.format(bigger, smaller ))
print('if ct == 1:\n'
      '     bigger = smaller = n\n'
    'else:\n'
        '   if n > bigger:\n'
        '   bigger = n\n'
        '   if n < smaller:\n'
        '   smaller = n')








