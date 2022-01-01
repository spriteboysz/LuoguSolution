#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-04 22:49:51
LastEditTime: 2021-11-04 23:01:21
Description: 
FilePath: CF440A.py
'''


def func():
    n = int(input())
    # *循环遍历TLE，通过等差数列求和
    total = sum(map(int, input().strip().split()))
    return n * (n + 1) // 2 - total


if __name__ == '__main__':
    ans = func()
    print(ans)
