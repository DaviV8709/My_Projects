print('Arithmetic Progression')
f1 = int(input('Enter the \033[31mfirst term\033[m: '))
r = int(input('Enter the \033[32mraison\033[m: '))
for c in range(f1, f1 + (10 - 1) * r, r):
    print('{} >'.format(c) , end=' ')
print('END')
