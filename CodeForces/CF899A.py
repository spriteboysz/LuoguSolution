#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 22:54:54
LastEditTime: 2021-11-27 23:51:43
Description: Splitting in Teams
FilePath: CF899A.py
'''


def func():
    n = int(input())
    num = list(map(int, input().strip().split()))
    a, b = num.count(1), num.count(2)
    count = 0
    if b > 0:
        if a >= b:
            count += b
            a -= b
            count += a // 3
        else:
            count += a
    else:
        count += a // 3
    print(count)


if __name__ == '__main__':
    func()
