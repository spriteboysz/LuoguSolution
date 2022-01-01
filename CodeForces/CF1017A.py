#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 23:49:42
LastEditTime: 2021-11-19 23:57:48
Description: The Rank
FilePath: CF1017A.py
'''


def func():
    n = int(input())
    point = []
    for _ in range(n):
        point.append(sum(map(int, input().strip().split())))
    smith = point[0]
    print(list(sorted(point, reverse=True)).index(smith) + 1)


if __name__ == '__main__':
    func()
