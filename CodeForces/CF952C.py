#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-08 22:48:52
LastEditTime: 2021-11-08 22:54:14
Description: Ravioli Sort
FilePath: CF952C.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    for i in range(n - 1):
        if abs(lst[i] - lst[i + 1]) > 1:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    func()
