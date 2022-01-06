#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-06 23:53:02
LastEditTime: 2022-01-07 00:04:26
Description: [USACO09NOV]The Grand Farm-off S
FilePath: P2965.py
'''


def func():
    n, a, b, c, d, e, f, g, h, m = map(int, input().strip().split())
    weight = [(a * i ** 5 + b * i ** 2 + c) % d for i in range(n * 3)]
    useful = [(e * i ** 5 + f * i ** 3 + g) % h for i in range(n * 3)]
    uw = sorted(zip(weight, useful), key=lambda el: (-el[1], el[0]))
    total = 0
    for i in range(n):
        total += uw[i][0]
    print(total % m)


if __name__ == '__main__':
    func()
