#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-09 22:51:12
LastEditTime: 2022-01-09 23:10:29
Description: [COCI2020-2021#6] Bold
FilePath: P7550.py
'''


def func():
    n, m = map(int, input().strip().split())
    info = [list(input().strip()) for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if info[i][j] == "#":
                info[i][j + 1], info[i + 1][j], info[i + 1][j + 1] = ["#"] * 3

    for row in info:
        print("".join(row))


if __name__ == '__main__':
    func()
