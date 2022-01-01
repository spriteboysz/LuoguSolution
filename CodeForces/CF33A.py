#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-27 22:14:20
LastEditTime: 2021-11-27 22:22:59
Description: What is for dinner?
FilePath: CF33A.py
'''


def func():
    n, m, k = map(int, input().strip().split())
    row = [1000000] * m
    for _ in range(n):
        r, c = map(int, input().strip().split())
        if row[r - 1] > c:
            row[r - 1] = c
    print(min(k, sum(row)))


if __name__ == '__main__':
    func()
