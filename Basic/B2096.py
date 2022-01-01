#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 17:49:36
Description: 直方图
FilePath: B2096.py
'''


def func():
    n = int(input())
    lst1 = list(map(int, input().strip().split()))
    lst2 = [0] * (max(lst1) + 1)
    for i in range(n):
        lst2[lst1[i]] += 1
    print("\n".join(map(str, lst2)))


if __name__ == '__main__':
    func()
