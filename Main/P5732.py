#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 13:21:17
LastEditTime: 2021-10-12 23:28:31
Description: 杨辉三角
FilePath: P5732.py
'''


def row(n):
    if n == 1:
        return [1]
    else:
        lst2 = []
        lst1 = row(n - 1)
        for i in range(len(lst1) - 1):
            lst2.append(lst1[i] + lst1[i + 1])
        return [1] + lst2 + [1]


def func():
    n = int(input().strip())
    for i in range(n):
        print(" ".join(map(str, row(i + 1))))


if __name__ == '__main__':
    func()
