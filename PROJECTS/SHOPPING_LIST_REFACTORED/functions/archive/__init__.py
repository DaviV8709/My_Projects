# CODES ABOUT ARCHIVE
from SHOPPING_LIST_REFACTORED.functions.data import *
from SHOPPING_LIST_REFACTORED.functions.show import *



def create_file():
    archive = 'list.txt'
    try:
        a = open(archive, 'x')
    except FileExistsError:
        print('Your file already exists')
        title('Showing it bellow', '\033[1;36m', 18, True)



def access_file(data = False): #ACCESS FILE/READ FILE
    try:
        archive = 'list.txt'
        a = open(archive, 'r')
        return archive if data else a
    except FileNotFoundError:
        create_file()


def write_file(old, new_content): #ABLE TO REWRITE/SUBSTITUTE INFO
    a = access_file().read()
    x = a.replace(old,new_content)
    z = open(access_file(True), 'w')
    z.write(x)


def append_file(info): #ABLE TO BUILD NEW INFOS
    a = open(access_file(True), 'a')
    a.write(info)


def find_info(info):
    a = access_file().readlines()
    for find in a:
        if info in find:
            return find