#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 16:13:41
Description: 查找特定的值
FilePath: B2093.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    x = int(input())

    for i in range(n):
        if lst[i] == x:
            print(i)
            break
    else:
        print(-1)


if __name__ == '__main__':
    func()
