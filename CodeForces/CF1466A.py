#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 22:36:31
LastEditTime: 2021-11-24 22:49:45
Description: Bovine Dilemma
FilePath: CF1466A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        point = list(map(int, input().strip().split()))
        distance = []
        for i in range(n - 1):
            for j in range(i + 1, n):
                distance.append(abs(point[i] - point[j]))
        print(len(set(distance)))


if __name__ == '__main__':
    func()
