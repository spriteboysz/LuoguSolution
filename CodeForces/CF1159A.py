#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-16 23:26:29
LastEditTime: 2021-11-16 23:29:51
Description: A pile of stones
FilePath: CF1159A.py
'''


def func():
    _ = int(input())
    s = input().strip()
    count = 0
    for item in s:
        if item == "-":
            count = max(0, count - 1)
        else:
            count += 1
    print(count)


if __name__ == '__main__':
    func()
