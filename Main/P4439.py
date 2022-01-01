#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 22:31:29
LastEditTime: 2021-10-22 22:35:47
Description: 
FilePath: P4439.py
'''


def func():
    n = int(input())
    lst = []
    for _ in range(n):
        color = input().strip()
        if len(lst) == 0 or color != lst[-1]:
            lst.append(color)
    print(len(lst) + 1)


if __name__ == '__main__':
    func()
