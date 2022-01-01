#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-26 17:24:24
LastEditTime: 2021-12-26 22:06:46
Description: JACK
FilePath: P6437.py
'''


def func():
    n, m = map(int, input().strip().split())
    lst = list(map(int, input().strip().split()))
    total = []
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if lst[i] + lst[j] + lst[k] <= m:
                    total.append(lst[i] + lst[j] + lst[k])
    print(max(total))


if __name__ == '__main__':
    func()
