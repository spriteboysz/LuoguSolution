#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-26 17:06:42
LastEditTime: 2021-12-26 23:17:23
Description: PROZORI
FilePath: P6438.py
'''


def func():
    n, m = map(int, input().strip().split())
    matrix = []
    row = [0] * m
    for i in range(n * 5 + 1):
        raw = list(input().strip()[1::5])
        if i % 5 != 0:
            for j in range(m):
                if raw[j] == "*":
                    row[j] += 1
        if i % 5 == 0 and i != 0:
            matrix.extend(row)
            row = [0] * m

    print(" ".join(map(lambda el: str(matrix.count(el)), range(5))))


if __name__ == '__main__':
    func()
