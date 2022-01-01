#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 22:42:04
Description: 同行列对角线的格 
FilePath: B2100.py
'''


def func():
    n, x, y = map(int, input().strip().split())
    # TODO: 如何生成这种空的列表？
    row = [[], [], [], []]
    for j in range(1, n + 1):
        row[0].append("(%d,%d)" % (x, j))

    for i in range(1, n + 1):
        row[1].append("(%d,%d)" % (i, y))

    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if i - j == x - y:
                row[2].append("(%d,%d)" % (i, j))
            if i + j == x + y:
                row[3].append("(%d,%d)" % (i, j))
    row[3] = reversed(row[3])

    for i in range(4):
        print(" ".join(row[i]))


if __name__ == '__main__':
    func()
