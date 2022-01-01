#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 22:34:11
LastEditTime: 2021-11-03 22:44:56
Description: Flag
FilePath: CF16A.py
'''


def func():
    n, m = map(int, input().strip().split())
    flag = []
    for i in range(n):
        row = list(map(int, list(input().strip())))
        if list(set(row)) * m != row:
            return "NO"
        flag.append(list(set(row)))
        if i > 0 and flag[i] == flag[i - 1]:
            return "NO"
    return "YES"


if __name__ == '__main__':
    ans = func()
    print(ans)
