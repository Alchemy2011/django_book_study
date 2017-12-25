# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
import re


def re_demo():
    source = "s2f程序员杂志一2d3程序员杂志二2d3程序员杂志三2d3程序员杂志四2d3"
    pattern = re.compile(r"([\u4e00-\u9fa5]+)")
    results = pattern.findall(source)
    for result in results:
        print(result)


if __name__ == '__main__':
    re_demo()
