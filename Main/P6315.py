#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-30 23:03:04
LastEditTime: 2021-12-30 23:29:34
Description: 
FilePath: P6315.py
'''


def func():
    base = {"A": [0, 0], "B": [0, 1], "C": [0, 2], "D": [0, 3],
            "E": [1, 0], "F": [1, 1], "G": [1, 2], "H": [1, 3],
            "I": [2, 0], "J": [2, 1], "K": [2, 2], "L": [2, 3],
            "M": [3, 0], "N": [3, 1], "O": [3, 2]}
    count = 0
    for i in range(4):
        row = list(input().strip())
        for j in range(4):
            if row[j] != ".":
                count += abs(i - base[row[j]][0]) + abs(j - base[row[j]][1])
    print(count)


if __name__ == '__main__':
    func()
