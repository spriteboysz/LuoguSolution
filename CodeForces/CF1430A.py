#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 23:35:41
LastEditTime: 2021-11-24 23:41:09
Description: Number of Apartments
FilePath: CF1430A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        flag = False
        for x in range(0, n // 3 + 1):
            for y in range(0, n // 5 + 1):
                if (n - 3 * x - 5 * y) % 7 == 0:
                    print(x, y, (n - 3 * x - 5 * y) // 7)
                    flag = True
                    break
            if flag:
                break
        else:
            print(-1)


if __name__ == '__main__':
    func()
