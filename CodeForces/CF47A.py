#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 23:02:55
LastEditTime: 2021-11-03 23:12:54
Description: Triangular numbers 
FilePath: CF47A.py
'''


def func():
    n = int(input())
    for i in range(n + 1):
        if i * (i + 1) == 2 * n:
            return "YES"
        elif i * (i + 1) > 2 * n:
            break
    return "NO"


if __name__ == '__main__':
    ans = func()
    print(ans)
