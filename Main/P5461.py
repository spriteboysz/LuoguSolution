#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-12 17:28:17
LastEditTime: 2021-12-12 17:58:27
Description: 赦免战俘
FilePath: P5461.py
'''


def absolve(matrix, x, y, length):
    if length % 2 == 0:
        length = length // 2
        for i in range(x, x + length):
            for j in range(y, y + length):
                matrix[i][j] = 0
        absolve(matrix, x + length, y, length)
        absolve(matrix, x, y + length, length)
        absolve(matrix, x + length, y + length, length)


def func():
    n = int(input())
    matrix = [[1] * 2 ** n for _ in range(2 ** n)]
    absolve(matrix, 0, 0, 2 ** n)

    for row in range(2 ** n):
        print(" ".join(map(str, matrix[row])))


if __name__ == '__main__':
    func()
