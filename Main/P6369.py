#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-04 23:07:14
LastEditTime: 2022-01-04 23:17:19
Description: MARATON
FilePath: P6369.py
'''


def func():
    n = int(input())
    chess = [["."] * (n + 4) for _ in range(n + 4)]
    for i in range(2, n + 2):
        chess[i][2: n + 2] = list(input().strip())

    for i in range(2, n + 2):
        for j in range(2, n + 2):
            if chess[i][j] != ".":
                if chess[i][j] == chess[i][j + 1] == chess[i][j + 2]:
                    print(chess[i][j])
                    return
                if chess[i][j] == chess[i + 1][j] == chess[i + 2][j]:
                    print(chess[i][j])
                    return
                if chess[i][j] == chess[i + 1][j + 1] == chess[i + 2][j + 2]:
                    print(chess[i][j])
                    return
                if chess[i][j] == chess[i + 1][j - 1] == chess[i + 2][j - 2]:
                    print(chess[i][j])
                    return
    print("ongoing")


if __name__ == '__main__':
    func()
