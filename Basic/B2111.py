#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-20 00:04:49
LastEditTime: 2021-10-20 00:08:34
Description: 基因相关性
FilePath: B2111.py
'''


def func():
    threshold = float(input())
    a = input().strip()
    b = input().strip()

    count = 0
    for i, j in zip(a, b):
        if i == j:
            count += 1
    if count / len(a) >= threshold:
        print("yes")
    else:
        print("no")


if __name__ == '__main__':
    func()
