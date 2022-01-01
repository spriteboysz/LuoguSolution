#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-27 22:24:08
LastEditTime: 2021-11-27 22:31:19
Description: Spit Problem
FilePath: CF29A.py
'''


def func():
    n = int(input())
    point, distance = [0] * n, [0] * n
    for i in range(n):
        point[i], distance[i] = map(int, input().strip().split())

    for i in range(n - 1):
        for j in range(i + 1, n):
            if point[i] + distance[i] == point[j] and point[j] + distance[j] == point[i]:
                print("YES")
                return
    else:
        print("NO")


if __name__ == '__main__':
    func()
