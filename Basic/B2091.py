#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 16:34:55
Description: 向量点积计算
FilePath: B2091.py
'''


def func():
    n = int(input())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))

    vectorproduct = 0
    for i, j in zip(a, b):
        vectorproduct += i * j
    print(vectorproduct)


if __name__ == '__main__':
    func()
