#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 22:40:11
LastEditTime: 2021-11-28 23:07:58
Description: 
FilePath: CF118B.py
'''


def func():
    n = int(input())
    for i in range(-n, n + 1):
        row = ""
        row += " " * (abs(i) * 2)
        row += " ".join(map(str, [x for x in range(0, (n - abs(i) + 1))]))
        row += " "
        row += " ".join(map(str, [x for x in range((n - abs(i) - 1), -1, -1)]))
        print(row.rstrip())


if __name__ == '__main__':
    func()
