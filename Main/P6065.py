#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-07 23:10:36
LastEditTime: 2022-01-07 23:36:23
Description: [USACO05JAN]Sumsets S
FilePath: P6065.py
'''


def func():
    n = int(input())
    if 0 < n <= 2:
        print(n)
    else:
        lst = [0] * (n + 1)
        lst[1], lst[2] = 1, 2
        mod = 10 ** 9
        for i in range(3, n + 1):
            lst[i] = lst[i - 1] % mod
            if i % 2 == 0:
                lst[i] += lst[i // 2] % mod
        print(lst[n] % mod)


if __name__ == '__main__':
    func()
