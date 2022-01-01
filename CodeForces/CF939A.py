#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 14:19:48
LastEditTime: 2021-11-26 14:26:23
Description: Love Triangle
FilePath: CF939A.py
'''


def func():
    n = int(input())
    f = list(map(int, input().strip().split()))
    for i in range(n):
        if f[f[f[i] - 1] - 1] == i + 1:
            print("YES")
            break
    else:
        print("NO")


if __name__ == '__main__':
    func()
