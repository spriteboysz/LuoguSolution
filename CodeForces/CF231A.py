#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-02 22:55:05
LastEditTime: 2021-11-02 22:57:32
Description: Team
FilePath: CF231A.py
'''


def func():
    n = int(input())
    count = 0
    for _ in range(n):
        row = sum(map(int, input().strip().split()))
        if row >= 2:
            count += 1
    return count


if __name__ == '__main__':
    ans = func()
    print(ans)
