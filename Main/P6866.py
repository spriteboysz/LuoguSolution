#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-24 22:28:28
LastEditTime: 2021-12-24 22:45:43
Description: Emacs
FilePath: P6866.py
'''


def func():
    n, m = map(int, input().strip().split())
    matrix = [["."] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        matrix[i + 1][1:-1] = list(input().strip())
        
    count = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if matrix[i][j] == "*":
                if matrix[i - 1][j] == "." and matrix[i][j - 1] == ".":
                    count += 1
    print(count)


if __name__ == '__main__':
    func()
