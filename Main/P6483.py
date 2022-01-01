#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-25 22:53:16
LastEditTime: 2021-12-25 23:35:48
Description: PARKET
FilePath: P6483.py
'''


def func():
    r, b = map(int, input().strip().split())
    for n in range(r // 2 + 1, 0, -1):
        m = r // 2 + 2 - n
        if (n - 2) * (m - 2) == b:
            print(n, m)
            break
    else:
        print(-1)


if __name__ == '__main__':
    func()
