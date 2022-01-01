#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 21:35:43
LastEditTime: 2021-11-21 21:42:13
Description: Maximum Increase
FilePath: CF702A.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    increase = [1] * n
    for i in range(1, n):
        if lst[i] > lst[i - 1]:
            increase[i] += increase[i - 1]
    print(max(increase))


if __name__ == '__main__':
    func()
