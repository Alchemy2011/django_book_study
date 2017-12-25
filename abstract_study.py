# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
import abc


class BasePizza(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def get_radius(self):
        """Method that should do something."""


if __name__ == '__main__':
    BasePizza()
