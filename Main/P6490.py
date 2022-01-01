#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-25 21:58:01
LastEditTime: 2021-12-25 22:05:19
Description: RAZINE
FilePath: P6490.py
'''


def func():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(int(input()))

    count = 0
    for i in range(n - 2, -1, -1):
        if lst[i] >= lst[i + 1]:
            count += lst[i] - lst[i + 1] + 1
            lst[i] = lst[i + 1] - 1
    print(count)


if __name__ == '__main__':
    func()
