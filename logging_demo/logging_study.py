# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
import logging


def simple_demo():
    logging.debug('hello')
    logging.info('I told you so')
    logging.warning('Watch out!')
    logging.error('error')
    logging.critical('danger')


def logging_to_a_file():
    logging.basicConfig(filename='example.log', filemode='w', level=logging.DEBUG)
    logging.debug('This message should go to the log file')
    logging.info('So should this')
    logging.warning('And this, too')

if __name__ == '__main__':
    # simple_demo()
    logging_to_a_file()
