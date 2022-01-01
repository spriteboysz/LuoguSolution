#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-19 17:43:55
LastEditTime: 2021-12-19 21:40:46
Description: Cytus-Holyknight
FilePath: P2067.py
'''


def func():
    n = int(input())
    matrix = []
    for i in range(n):
        row = list(input().strip())
        if row.count("1") >= 2:
            origin_y = i
        matrix.append(row)

    for i in range(n):
        
        for j in range(n):
            matrix[i][j]
            


if __name__ == '__main__':
    func()
    