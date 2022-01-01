#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-18 22:38:13
LastEditTime: 2021-12-18 23:11:34
Description: KRIŽALJKA
FilePath: P7765.py
'''


def func():
    a, b = input().strip().split()
    common = list(set(list(a)) & set(list(b)))
    for column in range(len(a)):
        if a[column] in common:
            break
    for row in range(len(b)):
        if b[row] in common:
            break
        
    #row, column = b.index(common), a.index(common)
    matrix = [["."] * len(a) for _ in range(len(b))]
    for i in range(len(b)):
        matrix[i][column] = b[i]
    for j in range(len(a)):
        matrix[row][j] = a[j]

    for row in matrix:
        print("".join(row))


if __name__ == '__main__':
    func()
