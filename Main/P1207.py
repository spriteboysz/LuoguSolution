#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-30 22:02:43
LastEditTime: 2021-10-30 22:21:17
Description: 双重回文数
FilePath: 1207.py
'''


import string


def transform(num, b):
    base = list(string.digits)
    lst = []
    while num > 0:
        num, mod = divmod(num, b)
        lst.append(base[mod])
    return "".join(lst[::-1])


def func():
    n, s = map(int, input().strip().split())
    num = s
    while True:
        if n == 0:
            break
        num += 1
        count = 0
        for b in range(2, 11):
            ss = transform(num, b)
            if ss == ss[::-1]:
                count += 1
                if count == 2:
                    print(num)
                    n -= 1
                    break


if __name__ == '__main__':
    func()
