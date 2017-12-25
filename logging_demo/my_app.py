# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
import logging

from logging_demo import my_lib


def main():
    logging.basicConfig(filename='my_app.log',
                        filemode='w',
                        format='%(asctime)s %(levelname)s:%(name)s:%(message)s',
                        # datefmt='%Y%m%d %I:%M:%S %p',
                        datefmt='%Y-%m-%d %H:%M:%S',
                        level=logging.INFO)
    logging.info('Started')
    my_lib.do_something()
    logging.info('Finished')
    logger = logging.getLogger(__name__)
    print(str(logger))


if __name__ == '__main__':
    main()
