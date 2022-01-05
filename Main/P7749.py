#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-05 23:54:13
LastEditTime: 2022-01-06 00:14:02
Description: [COCI2013-2014#2] MISA
FilePath: P7749.py
'''


def func():
    r, s = map(int, input().strip().split())
    matrix = [["."] * (s + 2) for _ in range(r + 2)]
    for i in range(r):
        matrix[i + 1][1:1 + s] = list(input().strip())

    count, maximum = 0, 0
    for i in range(1, r + 1):
        for j in range(1, s + 1):
            current = 0
            for m in range(-1, 2):
                for n in range(-1, 2):
                    if matrix[i + m][j + n] == "o":
                        current += 1
            if matrix[i][j] == "o":
                count += current - 1
            elif maximum < current:
                    maximum = current
    print(count // 2 + maximum)


if __name__ == '__main__':
    func()
