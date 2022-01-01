#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-18 14:36:04
LastEditTime: 2021-12-18 14:55:48
Description: Get Your Wish
FilePath: P7262.py
'''


def func():
    n, m, direction = input().strip().split()
    n, m = int(n), int(m)
    matrix = []
    for _ in range(n):
        matrix.append(list(input().strip()))

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == "o":
                path = []
                if direction == "v":
                    for x in range(i, n):
                        path.append(matrix[x][j])
                if direction == "^":
                    for x in range(0, i + 1):
                        path.append(matrix[x][j])
                if direction == ">":
                    for y in range(j, m):
                        path.append(matrix[i][y])
                if direction == "<":
                    for y in range(0, j + 1):
                        path.append(matrix[i][y])
                if "x" in path:
                    print("GG")
                    return
    print("OK")


if __name__ == '__main__':
    func()
