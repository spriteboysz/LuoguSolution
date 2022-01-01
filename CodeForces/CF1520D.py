#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 22:14:48
LastEditTime: 2021-11-26 22:17:32
Description: Same Differences
FilePath: CF1520D.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().strip().split()))
        count = 0
        for i in range(n - 1):
            for j in range(i + 1, n):
                if lst[j] - lst[i] == j - i:
                    count += 1
        print(count)


if __name__ == '__main__':
    func()
