#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-23 23:54:32
LastEditTime: 2021-12-24 00:03:03
Description: 三子棋II
FilePath: P1917.py
'''


def func():
    matrix = []
    for _ in range(3):
        matrix.extend(list(input().strip()))
    if "X" in [matrix[1], matrix[3], matrix[5], matrix[7]]:
        print("xiaoa will win.")
    else:
        print("Dont know.")
    print(matrix.count("X") + matrix.count("O"))


if __name__ == '__main__':
    func()
