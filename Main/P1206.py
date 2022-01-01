#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-30 21:42:38
LastEditTime: 2021-10-30 22:03:04
Description: 回文平方数
FilePath: P1206.py
'''


import string


def transform(num, b):
    base = list(string.digits + string.ascii_uppercase)
    lst = []
    while num > 0:
        num, mod = divmod(num, b)
        lst.append(base[mod])
    return "".join(lst[::-1])


def func():
    b = int(input())
    for i in range(1, 301):
        s = transform(i * i, b)
        if s == s[::-1]:
            print(transform(i, b), s)


if __name__ == '__main__':
    func()
