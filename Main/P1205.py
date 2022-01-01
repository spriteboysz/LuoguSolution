#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-09 23:55:54
LastEditTime: 2021-12-11 23:16:44
Description: 方块转换 Transformations
FilePath: P1205.py
'''


def transform1(square):
    n = len(square)
    square1 = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            square1[j][n - i - 1] = square[i][j]
    return (square1,)


def transform2(square):
    n = len(square)
    square2 = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            square2[n - i - 1][n - j - 1] = square[i][j]
    return (square2,)


def transform3(square):
    n = len(square)
    square3 = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            square3[n - j - 1][i] = square[i][j]
    return (square3,)


def transform4(square):
    n = len(square)
    square4 = [[0] * n for _ in range(n)]
    for i in range(0, n):
        for j in range(0, n):
            square4[i][n - j - 1] = square[i][j]
    return (square4,)


def transform5(square):
    n = len(square)
    square51 = [[0] * n for _ in range(n)]
    square52 = [[0] * n for _ in range(n)]
    square53 = [[0] * n for _ in range(n)]
    square54 = [[0] * n for _ in range(n)]
    square54 = transform4(square)
    square51 = transform1(square54[0])
    square52 = transform2(square54[0])
    square53 = transform3(square54[0])
    return (square51[0], square52[0], square53[0])


def transform6(square):
    return (square,)


def func():
    n = int(input())
    square, sq = [], []
    for _ in range(n):
        square.append(list(input().strip()))
    for _ in range(n):
        sq.append(list(input().strip()))
    transform = [transform1, transform2, transform3,
                 transform4, transform5, transform6]
    for i, fun in enumerate(transform):
        if sq in fun(square):
            print(i + 1)
            break
    else:
        print(7)


if __name__ == '__main__':
    func()
