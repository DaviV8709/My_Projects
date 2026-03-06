print('\033[1;33mSequence of Fibonacci\033[m')
#   0   1   1   2   3   5   8   13
#   t1  t2  t3
t1 = 0
t2 = 1
t3 = t1 + t2
count = 3
user = int(input('Terms: '))
print('0 >', end = ' ')
while count <= user: #IF USER IS SMALLER OR EQUAL TO COUNT | continue... |
    t1 = t2 #T1 NOW IS THE T2 VALUE
    t2 = t3 #T2 NOW IS THE T3 VALUE
    print(t3 , '>' , end = ' ')
    t3 = t1 + t2 # T3 IS EQUAL TO T2 + T1
    count = count + 1
print('END')
