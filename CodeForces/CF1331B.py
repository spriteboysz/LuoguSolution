#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-13 22:02:55
LastEditTime: 2021-11-13 22:06:43
Description: Limericks
FilePath: CF1331B.py
'''


def func():
    num = int(input())
    for i in range(2, num + 1):
        if num % i == 0:
            return str(i) + str(num // i)


if __name__ == '__main__':
    ans = func()
    print(ans)
