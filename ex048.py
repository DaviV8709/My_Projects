print('Challenge of {}Analysing{} & {}Counting{}'.format('\033[1;32m', '\033[m', '\033[1;34m', '\033[m'))
s = 0
ct = 0
for c in range(1,500, 2):
    if c % 3 == 0:
        ct = ct + 1 #CONTADOR |IMPORTANT |
        s = s + c #ACUMULADOR | IMPORTANT |
print('The {}sum{} between {}{}{} given is {}{}{}'
      .format( '\033[1;35m', '\033[m','\033[1;35m', ct,'\033[m', '\033[34m', s, '\033[m' ))
