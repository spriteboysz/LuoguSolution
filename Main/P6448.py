#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-25 23:48:22
LastEditTime: 2021-12-26 16:43:27
Description: A
FilePath: P6448.py
'''


def func():
    lst = list(map(int, input().strip().split()))
    for i in range(len(lst) - 1):
        for j in range(len(lst) - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                print(" ".join(map(str, lst)))


if __name__ == '__main__':
    func()
