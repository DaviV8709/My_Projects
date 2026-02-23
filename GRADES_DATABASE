print('\033[1;34mSTUDENTS GRADES\033[m')
print('-'*40)
info = []
num = 0
extra = ''
while True:
    student = [[], []]
    student[0].append(str(input('\033[1;37mEnter your name: \033[m')))
    student[1].append(float(input('Enter your \033[31mfirst grade: \033[m')))
    student[1].append(float(input('Enter your \033[32msecond grade: \033[m')))
    student[1].append((student[1][0] + student[1][1]) / 2 ) #AVERAGE
    info.append(student[:])
    student.clear()
    print('\033[1;35mMORE STUDENTS:\033[m\n'
          '\033[32m[ Y ] - YES\033[m\n'
          '\033[31m[ N ] - NO\033[m')
    question = str(input()).upper()
    while question not in 'YN':
        print('\033[31mYou entered an invalid option:\033[m\n'
              'Try again:')
        question = str(input()).upper()
    if question == 'N':
        break
    else:
        print('Next Student...')
print('\033[1;35mFYI [ AVERAGE ]\033[m\n'
      '\033[32m[ PASS ]\033[m - if Average \033[32mbigger than [ 8 ]\033[m\n'
      '\033[33m[ REMEDIAL CLASSES ]\033[m - if Average is \033[33mbetween [ 7 ] and [ 5 ]\033[m\n'
      '\033[31m[ FAIL ]\033[m - if Average \033[31mless than [ 5 ]\033[m')
while True:
    while extra != 'N':
        print('\033[37m[ NUMBER ]............[ NAME ].........[ AVERAGE ].......[ SITUATION ]\033[m')
        for student in info:
            num = num + 1
            print(f'{'':5}{num}{'':18}{student[0][0]}{'':15}{student[1][2]}{'':8}' ,
                  '\033[1;31mFAIL\033[m' if student[1][2] <= 4 else '',
                  '\033[1;33mREMEDIAL CLASSES\033[m' if student[1][2] <= 7 and student[1][2] >= 5 else '',
                  '\033[1;32mPASS\033[m' if student[1][2] >= 8 else '')
        print('\033[1;35mMore information: \033[32m[ Y ] \033[31m[ N ]\033[m')
        extra = str(input()).upper()
        while extra != 'Y' and extra != 'N':
            print('\033[1;35mEnter a valid option:\033[m')
            extra = str(input()).upper()
        if extra == 'Y':
            while extra == 'Y':
                print('\033[1;34mEnter the student number:\033[m ')
                number = int(input())-1
                print(f'\033[1;37mYou chose\033[36m[ {info[number][0][0]} ]\033[m')
                print(f'\033[1;31mFIRST GRADE:\033[1;35m[{info[number][1][0]}]\033[m\n'
                      f'\033[1;32mSECOND GRADE: \033[1;35m[{info[number][1][1]}]\033[m\n'
                      f'\033[37mAVERAGE: \033[1;35m[{info[number][1][2]}]\033[m\n')
                print('\033[36mOther student:\033[m\n'
                      '\033[1;32m[ YES ] \033[1;34| \033[1;31m[ NO ]\033[m')
                more = str(input()).upper()
                while more != 'Y' and more != 'N':
                    print('\033[1;31mEnter an valid option!\033[m')
                    more = str(input()).upper()
                if more == 'N':
                    extra = 'N'
        elif extra == 'N':
            extra = 'N'
    break
print('\033[1;4;32;40mThanks for using!\033[m')
