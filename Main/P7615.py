#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-15 23:36:32
LastEditTime: 2021-12-15 23:48:49
Description: OKRET
FilePath: P7615.py
'''


def func():
    r, c = map(int, input().strip().split())
    matrix = [["X"] * (c + 2) for _ in range(r + 2)]
    for i in range(1, r + 1):
        matrix[i][1:-1] = list(input().strip())

    for i in range(1, r + 1):
        for j in range(1, c + 1):
            if matrix[i][j] == ".":
                count = 0
                if matrix[i - 1][j] == "X":
                    count += 1
                if matrix[i + 1][j] == "X":
                    count += 1
                if matrix[i][j - 1] == "X":
                    count += 1
                if matrix[i][j + 1] == "X":
                    count += 1
                if count >= 3:
                    print(1)
                    return
    print(0)


if __name__ == '__main__':
    func()
