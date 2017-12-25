# -*- coding: utf-8 -*-
# __author__ = 'liqirong'


def write_read():
    with open('') as file_1,\
            open('', 'w') as file_2:
        file_2.write(file_1.read())

if __name__ == '__main__':
    write_read()
