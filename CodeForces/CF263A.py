#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 21:44:34
LastEditTime: 2021-11-05 21:51:55
Description: Beautiful Matrix
FilePath: CF263A.py
'''


def func():
    for i in range(5):
        row = list(map(int, input().strip().split()))
        if sum(row) == 1:
            x, y = i, row.index(1)
            
    print(abs(x - 2) + abs(y - 2))


if __name__ == '__main__':
    func()
