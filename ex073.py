print('\033[1;35m| CHALLENGE |\033[m \033[32mBrazilian \033[34mSoccer \033[33mTeams\033[m')
teams = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia', 'Athetico-PR', 'Bragatino', 'Chapecoense', 'Mirassol', 'Coritiba', 'Flamengo',
         'Botafogo', 'Corinthians', 'Grêmio', 'EC Vitória', 'Atlético- MG', 'Remo', 'Vasco da Gama', 'Santos', 'Internacional', 'Cruzeiro')
print(f'{"\033[31mBRASILEIRÃO \033[1;36m2026\033[m":^70}')
print('\033[1;35mWhat kind of info:\033[m\n'
      '\033[1;31m[ A ]\033[m- \033[31mFirst five\033[m\n'
      '\033[1;32m[ B ]\033[m- \033[32mLast four\033[m\n'
      '\033[1;33m[ C ]\033[m- \033[33mPut all teams in an Alphabetical order | A-Z |\033[m\n'
      '\033[1;34m[ D ]\033[m- \033[34mYours team position\033[m\n'
      '\033[1;35m[ E ]\033[m- \033[35mExit\033[m')
print('\033[1;37mSelect a option\033[m: ')
while True:
    choice = str(input()).upper()
    if choice == 'A':
        print('\033[1;31mThe first five\033[m are: ')
        for c in teams[:5]:
            print(f'\033[33m{teams.index(c)+1}ª\033[m \033[1;33m{c}\033[m')
        break
    elif choice == 'B':
        print('\033[32mThe last four\033[m are:')
        for c in teams[-4:]:
            print(f'\033[33m{teams.index(c)+1}ª\033[m \033[1;32m{c}\033[m')
        break
    elif choice == 'C':
        print('\033[1;33mAll in a alphabetical order\033[m')
        alpha = sorted(teams)
        for c in alpha:
            print(c)
        break
    elif choice == 'D':
        print('\033[1;36mEnter your team\033[m')
        team = str(input()).strip().capitalize()
        while team not in teams:
            if team not in teams:
                print('\033[1;31;40mINVALID!\033[m')
                print('\033[1;31mEnter another team:\033[m')
                team = str(input()).strip().capitalize()
        print(f'\033[1;36mYour team\033[m is \033[1;35m{team}\033[m and its on \033[1;33mthe position number\033[m \033[33m[ {teams.index(team)+1} ]ª\033[m')
        break
    elif choice == 'E':
        break
    else:
        print('\033[1;31mEnter a valid option\033[m')
print('\033[32m[ Thanks for using! ]\033[m')

