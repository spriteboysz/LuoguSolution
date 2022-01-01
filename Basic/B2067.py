#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 23:33:20
Description: 药房管理
FilePath: B2067.py
'''


def func():
    m = int(input())
    n = int(input())
    lst = list(map(int, input().strip().split()))

    count = 0
    for i in range(n):
        if m >= lst[i]:
            m -= lst[i]
        else:
            count += 1
    print(count)


if __name__ == '__main__':
    func()
