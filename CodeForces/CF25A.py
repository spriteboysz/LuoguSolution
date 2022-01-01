#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-27 23:00:14
LastEditTime: 2021-11-27 23:09:38
Description: IQ test
FilePath: CF25A.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    even = list(filter(lambda el: el % 2 == 0, lst))
    if len(even) == 1:
        print(lst.index(even[0]) + 1)
    else:
        odd = list(filter(lambda el: el % 2 != 0, lst))
        print(lst.index(odd[0]) + 1)


if __name__ == '__main__':
    func()
