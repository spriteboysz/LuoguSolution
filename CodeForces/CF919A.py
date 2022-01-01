#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 23:31:40
LastEditTime: 2021-11-19 23:36:22
Description: Supermarket
FilePath: CF919A.py
'''


def func():
    n, m = map(int, input().strip().split())
    price = []
    for _ in range(n):
        a, b = map(int, input().strip().split())
        price.append(a / b)
    print("%.8f" % (m * min(price)))


if __name__ == '__main__':
    func()
