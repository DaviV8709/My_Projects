def archiveExist(name):
    try:
        a = open(name, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def archiveCreate(name):
    try:
        a = open(name, 'wt+')
        a.close()
    except:
        print('Error found')
    else:
        print(f'Archive {name} created')


def archiveRead(name):
    try:
        a = open(name, 'rt')
    except:
        print(f'\033[1;31;40m{"NO INFOS ENTERED":^40}\033[m')
    else:
        print(f'\033[1;33m{"[ NAME ]":>10}\033[1;32m{"[ AGE ]":^19}\033[1;37m{"[ GENDER ]"}\033[m')
        print(f'{a.read()}')

def archiveWrite(name, content=''):
    try:
        a = open(name,  'at')
    except:
        print(f'Creating {name}...')
        archiveCreate(name)
    else:
        a.write(f'{content}')
        print('Content SAVED')
    finally:
        a.close()


