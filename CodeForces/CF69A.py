#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 23:27:51
LastEditTime: 2021-11-05 23:34:34
Description: Young Physicist
FilePath: CF69A.py
'''


def func():
    n = int(input())
    matrix = []
    for _ in range(n):
        matrix.append(list(map(int, input().strip().split())))
        
    x, y, z = 0, 0, 0
    for el in matrix:
        x += el[0]
        y += el[1]
        z += el[2]
    if x == y == z == 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
    