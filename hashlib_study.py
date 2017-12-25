# -*- coding: utf-8 -*-
# __author__ = 'liqirong'
import hashlib
import os


# 较小文件的处理方法
def get_md5_small(file_path):
    md5 = None
    if os.path.isfile(file_path):
        f = open(file_path, 'rb')
        md5_obj = hashlib.md5()
        md5_obj.update(f.read())
        hash_code = md5_obj.hexdigest()
        f.close()
        md5 = str(hash_code).lower()
    return md5


# 较大文件的处理方法
def get_md5_big(file_path):
    f = open(file_path, 'rb')
    md5_obj = hashlib.md5()
    while True:
        d = f.read(8096)
        if not d:
            break
        md5_obj.update(d)
    hash_code = md5_obj.hexdigest()
    f.close()
    md5 = str(hash_code).lower()
    return md5

if __name__ == '__main__':
    file_path2 = r'D:\PycharmProjects\20171005\self_study\decorator_study.py'
    md5_01 = get_md5_small(file_path2)
    print(md5_01)
    md5_02 = get_md5_big(file_path2)
    print(md5_02)
    """
    m = hashlib.md5()
    m.update(b"Nobody inspects")
    m.update(b" the spanish repetition")
    print(m.digest())
    print(m.hexdigest())
    print(m.digest_size)
    print(m.block_size)
    """
