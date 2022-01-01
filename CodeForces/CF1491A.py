#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-25 23:25:53
LastEditTime: 2021-11-26 13:51:26
Description: K-th Largest Value
FilePath: CF1491A.py
'''


def func():
    n, q = map(int, input().strip().split())
    lst = list(map(int, input().strip().split()))
    count = lst.count(1)
    for _ in range(q):
        t, xk = map(int, input().strip().split())
        if t == 1:
            if lst[xk - 1] == 0:
                count += 1
            else:
                count -= 1
        elif t == 2:
            print(0 if xk > count else 1)


if __name__ == '__main__':
    func()
