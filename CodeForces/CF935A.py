#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 14:28:15
LastEditTime: 2021-11-26 14:32:15
Description: Fafa and his Company
FilePath: CF935A.py
'''


def func():
    n = int(input())
    count = 0
    for i in range(1, n):
        if n % i == 0:
            count += 1
    print(count)


if __name__ == '__main__':
    func()
    