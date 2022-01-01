#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 22:41:36
Description: 与7无关的数
FilePath: B2081.py
'''


def func():
    n = int(input())

    total = 0
    for i in range(1, n + 1):
        if i % 7 == 0 or str(i).count("7") > 0:
            continue
        total += i * i
    print(total)


if __name__ == '__main__':
    func()
