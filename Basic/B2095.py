#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 17:10:25
Description: 白细胞计数
FilePath: B2095.py
'''


def func():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(float(input().strip()))

    lst.remove(min(lst))
    lst.remove(max(lst))
    average = sum(lst) / len(lst)

    error = 0
    for item in lst:
        if abs(item - average) > error:
            error = abs(item - average)
    print("%.2f %.2f" % (average, error))


if __name__ == '__main__':
    func()
