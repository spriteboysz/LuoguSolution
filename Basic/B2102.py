#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-10 22:11:31
LastEditTime: 2021-12-10 22:30:20
Description: 计算鞍点
FilePath: B2102.py
'''


def func():
    matrix = []
    for _ in range(5):
        matrix.append(list(map(int, input().strip().split())))

    for i in range(5):
        maximum = max(matrix[i])
        column = matrix[i].index(maximum)
        lst = []
        for j in range(5):
            lst.append(matrix[j][column])
        minimun = min(lst)
        if maximum == minimun:
            row = lst.index(minimun)
            print(row + 1, column + 1, matrix[row][column])
            break
    else:
        print("not found")


if __name__ == '__main__':
    func()
