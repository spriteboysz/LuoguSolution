#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-19 23:27:14
LastEditTime: 2021-12-19 23:47:56
Description: 轰炸III
FilePath: P1830.py
'''


def func():
    n, m, x, y = map(int, input().strip().split())
    matrix = [[[0] * 2 for _ in range(m)] for _ in range(n)]
    for i in range(x):
        x1, y1, x2, y2 = map(int, input().strip().split())
        for row in range(x1, x2 + 1):
            for column in range(y1, y2 + 1):
                matrix[row - 1][column - 1][0] += 1
                matrix[row - 1][column - 1][1] = i + 1

    for _ in range(y):
        row, column = map(int, input().strip().split())
        row, column = row - 1, column - 1
        if matrix[row][column][0] != 0:
            print("Y", matrix[row][column][0], matrix[row][column][1])
        else:
            print("N")


if __name__ == '__main__':
    func()
