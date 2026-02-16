print('\033[1;35mCounting \033[1;34mVowels\033[m')
words = ('Punk', 'Music', 'Happiness', 'Sing', 'Shirt', 'Love', 'Felling', 'Study', 'Video', 'Unlock')
for word in words:
    print(f'\nIn the \033[1;31mword \033[1;32m{word.upper()}\033[m there is', end = ' ')
    for letter in word.lower():
        if letter in 'aeiou':
            print(f'\033[1;34m[ {letter} ]\033[m', end =' ')
print('\nWanna test: \033[1;32m[ Y ]\033[m \033[1;31m[ N ]\033[m')
question = str(input()).upper()
while True:
    if question == 'Y':
        print('\033[1;36mEnter a word\033[m:')
        word = str(input()).strip().lower()
        print(f'Your \033[1;36mword\033[m is \033[1;35m[ {word.capitalize()} ]\033[m, and there is' , end = ' ')
        for letter in word:
            if letter in 'aeiou':
                print(f'\033[1;34m[ {letter} ]\033[m', end =' ')
        print('\n\033[1;34mAnother word\033[m: \033[1;32m[ Y ] \033[1;31m[ N ]\033[m')
        question1 = ''
        while question1 != 'N' and question1 != 'Y':
            question1 = str(input()).upper()
            if question1 == 'N':
                question = 'N'
            elif question1 == 'Y':
                print('Next...')
                question = 'Y'
            else:
                print('Enter a valid option')
    elif question == 'N':
        break
    else:
        print('\033[1;31mEnter a valid option\033[m')
        question = str(input()).upper()
print('\033[32m[ Thanks for using! ]\033[m')
