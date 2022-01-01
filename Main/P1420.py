#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 22:46:56
Description: 最长连号
FilePath: P1420.py
'''


def func():
    n = int(input())
    lst1 = list(map(int, input().strip().split()))
    lst2 = ["0"] * n
    for i in range(1, n):
        if lst1[i] - lst1[i - 1] == 1:
            lst2[i] = str(lst1[i] - lst1[i - 1])

    print(max(map(len, "".join(lst2).split("0"))) + 1)


if __name__ == '__main__':
    func()
