from functions.archive import *
from functions.data import *
from functions.show import *

create_file()

while True:
    title('SHOPPING LIST', '\033[1;35m', 25, True)
    menu()
    choice = str(input())
    if choice == '1':
        # PRODUCTS AREA
        title('PRODUCTS ALREADY ENTERED', '\033[1;32m')
        print(f'{products_list()}' if len(products_list(True)) != 0 else '\033[1;31;40m[ No products entered ]\033[m')
        title('PRODUCT AREA', '\033[1;32m', 15, True)
        print('[1] Enter a new Product\n'
              '[2] Delete a Product')
        product = str(input())
        while product not in ('1','2'):
            product = str(input('Please enter a valid option\n'))
        if product == '1':
            while True:
                a = add_product()
                if a == 'Nothing':
                    title('Exiting...\n'
                          'Going back to the main menu', '\033[1;31m')
                    break
                title(f'You added [{a[0]}] as a product successfully', '\033[1;32m')
                product_file(a, True)
                more = str(input('\033[1;34mAdd more products?\033[m\n'
                                 '\033[32m[ 1 ] - YES\n'
                                 '\033[31m[ 2 ] - NO\033[m\n'))
                if more == '2':
                    break
        elif product == '2':
            remove = remove_product()
            if remove == 'Nothing':
                title('Exiting...\n'
                      'Going back to the main menu', '\033[1;31m')
                break
            product_file(remove, False, True)

    elif choice == '2':
        # CATEGORIES AREA
        title('CATEGORIES ALREADY ENTERED', '\033[1;32m')
        print(f'{categories_list()}' if len(categories_list(True)) != 0 else '\033[1;31;40m[ No categories entered ]\033[m')
        title('CATEGORIES AREA', '\033[1;32m', 15, True)
        print('[1] Enter a new category\n'
              '[2] Delete a category')
        category = int(input())
        while category not in ('2', '1'):
            category = str(input('Please enter a valid option\n'))
        if category  == '1':
            while True:
                a = add_category()
                if a == 'Nothing':
                    title('Exiting...\n'
                          'Going back to the main menu', '\033[1;31m')
                    break
                title(f'You added [{a}] as a category successfully', '\033[32m')
                category_file(a, True)
                more = str(input('\033[1;34mAdd more categories?\033[m\n'
                                 '\033[32m[ 1 ] - YES\n'
                                 '\033[31m[ 2 ] - NO\033[m\n'))
                if more == '2':
                    break
        elif category == '2':
            remove = remove_category()
            if remove == 'Nothing':
                title('Exiting...\n'
                      'Going back to the main menu', '\033[1;31m')
            else:
                title(f'You deleted {remove} Category successfully', '\033[31m')
                category_file(remove, False, True)
    elif choice == '3':
        break
    else:
        title('You entered an invalid option', '\033[1;31m', 20, True)


print('\033[1;32mThanks For Using!\n'
      'Developed By\n'
      '\033[40mDavi S.\033[m')