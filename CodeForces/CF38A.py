#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-12 22:45:10
LastEditTime: 2021-11-12 22:49:20
Description: Army 
FilePath: CF38A.py
'''


def func():
    n = int(input())
    d = list(map(int, input().strip().split()))
    a, b = map(int, input().strip().split())
    year = 0
    for i in range(a, b):
        year += d[i - 1]
    print(year)


if __name__ == '__main__':
    func()
