#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-09 23:39:18
LastEditTime: 2021-11-09 23:46:16
Description: 
FilePath: CF900A.py
'''


def func():
    n = int(input())
    points = []
    for _ in range(n):
        x, y = map(int, input().strip().split())
        points.append(x)
    left, right = 0, 0
    for item in points:
        if item < 0:
            left += 1
        elif item > 0:
            right += 1
    if left <= 1 or right <= 1:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
    