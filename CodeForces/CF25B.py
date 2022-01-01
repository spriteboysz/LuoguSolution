#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-27 22:34:18
LastEditTime: 2021-11-27 22:51:08
Description: Phone number
FilePath: CF25B.py
'''


def func():
    n = int(input())
    phone1 = input().strip()
    init = 2 if n % 2 == 0 else 3
    phone2 = phone1[:init]
    for i in range(init, n):
        if (i - init) % 2 == 0:
            phone2 += "-" + phone1[i]
        else:
            phone2 += phone1[i]
    print(phone2)


if __name__ == '__main__':
    func()
