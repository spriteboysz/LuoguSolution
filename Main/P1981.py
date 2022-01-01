#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-15 22:53:46
LastEditTime: 2021-12-15 23:10:43
Description: 表达式求值
FilePath: P1981.py
'''


def func():
    s = input().strip()
    lst = list(s.replace("-", "+-").lstrip("+").split("+"))
    value = 0
    for el in lst:
        if "*" in el:
            v = 1
            for item in list(el.split("*")):
                v *= int(item)
            value += v
        else:
            value += int(el)
    print(value % 10000)


if __name__ == '__main__':
    func()
