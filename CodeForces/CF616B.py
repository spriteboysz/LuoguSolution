#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-18 23:19:45
LastEditTime: 2021-11-18 23:25:54
Description: Dinner with Emma
FilePath: CF616B.py
'''


def func():
    n, _ = map(int, input().strip().split())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))
    #*每行中最小的数字中选最大值
    print(max(map(min, matrix)))


if __name__ == '__main__':
    func()
