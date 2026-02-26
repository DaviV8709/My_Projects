print('\033[35;40mReading soccer player data\033[m')
team = list()
player = dict()
gols = list()
games = ('\033[1;31mFIRST\033[m', '\033[1;32mSECOND\033[m', '\033[1;33mTHIRD\033[m', '\033[1;34mFOURTH\033[m')
while True:
    player['Name'] = str(input('\033[1;35mName:\033[m ')).capitalize().strip()
    player['Country'] = str(input('\033[1;32mEnter the players Country:\033[m ')).capitalize().strip()
    game = int(input('\033[1;34mGames:\033[m '))
    print('Enter the \033[1;33m[ score ]\033[m of each Game: ')
    for c in range(0, game):
        gols.append(int(input(f'  >>>>>\033[38mEnter the \033[1;35mScore of the\033[m {games[c]} Game: ' if game <=4 else f'\033[1;38mGAME {c+1}:\033[m ')))
    player['Gols'] = gols[:]
    player['Score'] = sum(gols)
    team.append(player.copy())
    player.clear()
    gols.clear()
    more = str(input('\033[1;35mMore players: \033[32m[ Y ] \033[34m| \033[31m[ N ]\033[m')).upper()
    while more not in 'YN':
        print('You entered an invalid option\n'
              'Enter it again:')
        more = str(input()).upper()
    if more == 'N':
        break
    print('Next Player.....')
print('=-'*20)
choice = 'L'
while choice == 'L':
    print('   [ NAME ]           [ COUNTRY ]         [ TOTAL SCORE ]')
    for player in team:
        print(f'{player['Name']:^15}{player['Country']:^25}{player['Score']:^19}')
    print('\033[1;35mExtra Info Players:\033[m\n'
          '\033[1;32m[ Y ] \033[1;31m[ N ]\033[m')
    extra = str(input()).upper()
    while extra != 'N' and extra != 'Y':
        print(f'\033[31;40m[{extra}]\033[m is \033[1;31mnot a valid option:\033[m \n'
              'Enter it again: \033[1;32m[ Y ] \033[1;31m[ N ]\033[m')
        extra = str(input()).upper()
    print('=-'*20)
    ct = len(team)
    if extra == 'Y':
        print('\033[1;34mEnter the players Name: \033[m')
        choice = 'V'
        while choice == 'V':
            name = str(input()).capitalize().strip()
            for player in team:
                if player['Name'] == name:
                    print('<'*10 , f'\033[1;38mAll about: {name}\033[m', '>'*10)
                    for check in team:
                        if check['Name'] == name:
                            for key, value in player.items():
                                print(f'\033[1;38m{key}\033[m: \033[1;37m{value}\033[m')
                    print('\033[34m[ EACH GAME ] \033[35mINFORMATION\033[m')
                    for info in team:
                        if info['Name'] == name:
                            for i, v in enumerate(player['Gols']):
                                print(f'  >>>>>On the \033[37m{i+1}ªGAME,\033[m\033[1;36m [ {name} ]\033[m scored {v} points')
                    print('\033[35m[ V ] - VIEW OTHER PLAYERS\033[m\n'
                          '\033[33m[ L ] - LIST\033[m\n'
                          '\033[31m[ E ] - EXIT\033[m')
                    choice = str(input()).upper()
                    if choice == 'E':
                        break
                    elif choice == 'L':
                        break
                    elif choice == 'V':
                        print('\033[1;34mEnter the players Name:\033[m ')
                else:
                    ct = ct - 1
                    if ct == 0:
                        print(f'\033[31;40m[{name}]\033[m were \033[31mnot at the list\n'
                              '\033[1;31mPlease enter it again:\033[m ')
                        ct = len(team)
    else:
        break
print('\033[1;32;40mThanks for Using!\033[m')
