#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-31 22:25:47
LastEditTime: 2021-12-31 22:42:58
Description: 儒略の日
FilePath: P7902.py
'''


def func():
    n, d = map(int, input().strip().split())
    if n % 2 == 1:
        even, odd = n - 1, (n - 1) // 2 + 1
    else:
        even, odd = n, n // 2

    if even + odd >= d + 1:
        for i in range(1, n + 1, 2):
            print(i, end=" ")
        for i in range(2, n + 1, 2):
            print(i, i, end=" ")
        for i in range(1, n + 1, 2):
            print(i, end=" ")
        print()
    else:
        print(-1)


if __name__ == '__main__':
    func()
