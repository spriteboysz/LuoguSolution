#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-04 23:50:47
LastEditTime: 2021-11-04 23:58:11
Description: On Segment's Own Points
FilePath: CF397A.py
'''


def func():
    base = [1] * 101
    n = int(input())
    a1, b1 = map(int, input().strip().split())
    for _ in range(n - 1):
        a, b = map(int, input().strip().split())
        base[a:b+1] = [0] * (b - a + 1)
    return sum(base[a1:b1+1])


if __name__ == '__main__':
    ans = func()
    print(ans)
