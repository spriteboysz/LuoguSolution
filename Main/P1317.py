#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-08 00:03:10
LastEditTime: 2021-12-09 23:48:28
Description: 低洼地
FilePath: P1317.py
'''


def func():
    n = int(input())
    height = list(map(int, input().strip().split()))
    left = False
    count = 0
    for i in range(n - 1):
        if height[i] > height[i + 1]:
            left = True
        if height[i] < height[i + 1] and left == True:
            count += 1
            left = False
    print(count)


if __name__ == '__main__':
    func()
