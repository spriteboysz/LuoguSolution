#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-05 15:50:06
LastEditTime: 2021-12-05 15:57:28
Description: First Step
FilePath: P3654.py
'''


def func():
    row, column, k = map(int, input().strip().split())
    matrix = []
    for _ in range(row):
        matrix.append(list(input().strip()))

    for item in matrix:
        for i in range(column):
            if item[i] == ".":
                pass
            


if __name__ == '__main__':
    func()
    