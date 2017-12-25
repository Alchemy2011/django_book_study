# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
# strip不仅可以去除两端的空白，还能去除两端的指定字符
# 循环去除指定字符，一旦不存在指定字符则停止
if __name__ == '__main__':
    string = 'hello world'
    print(string.strip('hello'))
    print(string.strip('hello').strip())
    print(string.strip('heldo').strip())

    stt = 'h1h1h2h3h4h'
    print(stt.strip('h1'))

    s = '123459947855aaaadgat134f8sfewewrf7787789879879'
    print(s.strip('0123456789'))
