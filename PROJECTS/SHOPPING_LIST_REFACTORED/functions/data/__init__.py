# CODES TO DEVELOP THE ORGANIZE INFO
from SHOPPING_LIST_REFACTORED.functions.show import *
from SHOPPING_LIST_REFACTORED.functions.archive import *
from time import sleep


def menu():
    options()
    write_table()


def write_table():
    check = 'nothing'
    a = access_file()
    for x in a:
        check = check + x
    if check == 'nothing':
        append_file('[category]\n'
                    '[product]\n'
                    f'{'-' * 42}\n'
                    f'{'[ NAME ]'}{'[ CATEGORY ]':^24}{'[ AMOUNT ]'}\n')


def options():
    x = ['Products', 'Categories', 'Exit']
    for i, n in enumerate(x):
        print(f'[ {i + 1} ] {n}')

# FUNCTIONS ABOUT PRODUCTS

def products_list(words = False):
    letter = ''
    x_inlist = []
    a = access_file()
    x = a.readlines()[1]
    for each in x:
        letter = letter + each
        if each == ' ':
            x_inlist.append(letter.strip())
            letter = ''
    return x_inlist if words else x


def add_product():
    product = list()
    name = str(input('[NAME]:\n'))
    while name.upper() in products_list(True) or name.upper() in categories_list(True):
        print(f'{name.capitalize()} is already a', 'product' if name.upper() in products_list(True) else 'category')
        name = str(input('Enter other option:'))
    product.append(name.capitalize())
    if len(categories_list(True)) == 0:
        title('First enter a Category, then come back!', '\033[1;35m')
        return 'Nothing'
    print(f'Categories \n{categories_list()}')
    category = str(input('[CATEGORY]:\n')).upper()
    while category not in categories_list(True):
        title(f'[{category}] is an invalid category. Please enter it again', '\033[1;31m')
        category = str(input(f'CATEGORIES AVAILABLE: \n{categories_list()}>> ')).upper()
    product.append(category.capitalize())
    product.append(int(input('[AMOUNT]:\n')))
    sure = str(input(f'Are you sure about adding {name.capitalize()} in CATEGORY: [{category}]?\n'
                     f'[YES] / [NO]\n')).upper()
    while sure != 'YES' and sure != 'NO':
        sure = str(input('Please enter a valid option\n')).upper()
    if sure == 'NO':
        return 'Nothing'
    elif sure == 'YES':
        return product


def remove_product():
    print('Deleting a product')
    delete = str(input('Product to delete\n')).capitalize()
    while delete.upper() not in products_list(True):
        delete = str(input(f'{delete} is not a valid product. Enter another option'))
    sure = str(input(f'Are you sure about deleting {delete}, and all its infos\n'
                     '[ YES ]\n'
                     '[ NO ]\n'))
    while sure.upper() not in ('YES', 'NO'):
        sure = str(input('You entered an invalid option. Enter it again:'))
    if sure.upper() == 'NO':
        return 'Nothing'
    else:
        return delete


def checking_products():
    words = products_list(True)
    ct = 0
    for each in words:
        if find_info(each):
            ct = ct + 1
        if find_info(each.capitalize()):
            ct = ct + 1
        if ct != 2:
            write_file(f'{each} ', '')

def remove_product_file(info):
    delete = find_info(info)
    write_file(delete, '')


def add_product_file(info):
    write_file(f'[{info[1].lower()}]', f'{info[0]:18}{info[1]}{info[2]:>15}\n[{info[1].lower()}]')

def product_main_file(info):
    write_file('[product]', f'{info[0].upper()} [product]')


def product_file(product, add = False, remove = False):
    if add:
        product_main_file(product)
        add_product_file(product)
    if remove:
        remove_product_file(product)
        write_file(f'{product.upper()} ', '')


# FUNCTIONS ABOUT CATEGORIES

def categories_list(words = False):
    letter = ''
    x_inlist = []
    a = access_file()
    x = a.readlines()[0]
    for each in x:
        letter = letter + each
        if each == ' ':
            x_inlist.append(letter.strip())
            letter = ''
    return x_inlist if words else x


def add_category():
    while True:
        name = str(input('Enter a New Category: \n')).capitalize()
        while name.upper() in products_list(True) or name.upper() in categories_list(True):
            print(f'{name.capitalize()} is already a', 'product' if name.upper() in products_list(True) else 'category')
            name = str(input('Enter other option:'))
        sure = str(input(f'Are you sure about adding {name.capitalize()}?\n'
                         f'[YES] / [NO]\n'))
        while sure.upper() != 'YES' and sure != 'NO':
            sure = str(input('Please enter a valid option\n'))
        if sure == 'NO':
            return 'Nothing'
        else:
            return name


def remove_category():
    if len(categories_list(True)) == 0:
        print('You entered no categories. Enter at least one category first')
        return 'Nothing'
    else:
        print('Deleting a whole category')
        delete = str(input('Category to delete\n')).capitalize()
        while delete.upper() not in categories_list(True):
            delete = str(input(f'{delete} is not a category. Enter a valid category'))
        sure = str(input(f'Are you sure about deleting {delete}, and all its products?\n'
                         '[ YES ]\n'
                         '[ NO ]\n'))
        while sure.upper() not in ('YES', 'NO'):
            sure = str(input('You entered an invalid option. Enter it again:'))
        if sure.upper() == 'NO':
            return 'Nothing'
        else:
            return delete


def remove_category_file(info):
    while True:
        try:
            a = find_info(info)
        except Exception as error:
            print(error)
        else:
            try:
                write_file(a, '')
            except TypeError: #FUNTION TRY TO REMOVE AN INEXISTENT INFO
                break
    write_file(f'{'=' * 43}\n[{info.lower()}]\n', '')
    checking_products()



def add_category_file(info):
   append_file(f'{'=' * 43}\n{' ':18}{info.capitalize()}\n[{info.lower()}]\n')


def category_main_file(info):
    write_file('[category]', f'{info.upper()} [category]')


def category_file(category, add = False, remove = False):
    if add:
        add_category_file(category)
        category_main_file(category)
    if remove:
        remove_category_file(category.capitalize())
        write_file(f'{category.upper()} ', '')