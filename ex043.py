print('Challenge of BMI\n'
      'Body Mass Index')
print('CONSIDERING 7 categories: \n'
      '{}UNDERWEIGHT{}\n'
      '{}NORMAL{}\n'
      '{}OVERWEIGHT{}\n'
      '{}OBESE{}\n'
      '{}DANGEROUS OBESITY{}\n'
      .format('\033[1;31m' , '\033[m', '\033[1;32m', '\033[m', '\033[1;34m', '\033[m', '\033[1;36m', '\033[m', '\033[1;31m', '\033[m'))
h = float(input('Enter your \033[1;31mheight\033[m in \033[1;36m(m):\033[m' ))
w = float(input('Enter your \033[1;34mweight\033[m in \033[1;36m(kg):\033[m '))
bmi = w / (h ** 2)
if bmi <18.5:
    print('Your BMI is {}{:.2f}{}, and your category is {}UNDERWEIGHT{}'
          .format('\033[1;35m', bmi, '\033[m', '\033[31m', '\033[m'))
elif 18.5 <= bmi < 25:
    print('Your BMI is {}{:.2f}{}, and your category is {}NORMAL{}'
          .format('\033[1;35m', bmi , '\033[m', '\033[1;32m', '\033[m'))
elif 25 <= bmi <30:
    print('Your BMI is {}{:.2f}{}, and your category is {}OVERWEIGHT{}'
          .format('\033[1;35m', bmi, '\033[m', '\033[1;34m', '\033[m'))
elif 30 <= bmi < 40:
    print('Your BMI is {}{:.2f}{}, and your category is {}OBESE{}'
          .format('\033[1;35m', bmi, '\033[m', '\033[1;36m', '\033[m'))
elif bmi > 40:
    print('Your BMI is {}{:.2f}{}, and your category is {}DANGEROUS OBESITY{}'
          .format('\033[1;35m', bmi, '\033[m', '\033[1;31m', '\033[m'))

