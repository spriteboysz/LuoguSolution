#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-23 22:08:14
LastEditTime: 2021-10-23 22:10:02
Description: Another Cow Number Game G
FilePath: P6206.py
'''


def func():
    n = int(input())

    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        count += 1

    print(count)


if __name__ == '__main__':
    func()
