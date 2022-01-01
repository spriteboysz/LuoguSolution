#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-03 22:15:49
LastEditTime: 2021-12-03 22:27:18
Description: Insomnia cure
FilePath: CF148A.py
'''


def func():
    k, l, m, n, d = int(input()), int(input()), int(
        input()), int(input()), int(input())

    count = 0
    for i in range(1, d + 1):
        if i % k == 0 or i % l == 0 or i % m == 0 or i % n == 0:
            count += 1
    print(count)


if __name__ == '__main__':
    func()
