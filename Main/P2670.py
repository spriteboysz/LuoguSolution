#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-12 16:26:02
LastEditTime: 2021-12-12 17:17:10
Description: 扫地雷
FilePath: P2670.py
'''


def func():
    n, m = map(int, input().strip().split())
    matrix = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(1, n + 1):
        row = list(input().strip())
        for j in range(1, m + 1):
            if row[j - 1] == "*":
                matrix[i][j] = row[j - 1]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i][j] == "*":
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if matrix[i + x][j + y] != "*":
                            matrix[i + x][j + y] += 1

    for i in range(1, n + 1):
        print("".join(map(str, matrix[i][1:-1])))


if __name__ == '__main__':
    func()
