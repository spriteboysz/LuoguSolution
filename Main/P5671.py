#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-24 23:27:05
LastEditTime: 2021-12-24 23:45:26
Description: Triangles
FilePath: P5671.py
'''


def func():
    x, m, n = map(int, input().strip().split())
    if x % 2 == 0:
        lst1 = sorted(list({x // 2, x, 180 - x * 2, (180 - x) // 2}))
        print(" ".join(map(str, lst1)))
    else:
        lst1 = sorted(list({x / 2, x, 180 - x * 2, (180 - x) / 2}))
        print(" ".join(map(lambda el: "%.1f" %
              el if el * 10 % 10 != 0 else str(el), lst1)))

    if m == n:
        lst2 = (n * n + m * m) ** 0.5
        print("%.5f" % lst2)
    else:
        lst2 = sorted(list({(n * n - m * m) ** 0.5, (n * n + m * m) ** 0.5}))
        print(" ".join(map(lambda el: "%.5f" % el, lst2)))


if __name__ == '__main__':
    func()
