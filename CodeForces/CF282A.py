#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 21:34:35
LastEditTime: 2021-11-05 21:40:51
Description: Bit++
FilePath: CF282A.py
'''


def func():
    n = int(input())
    count = 0
    for _ in range(n):
        s = input().strip()
        if "++" in s:
            count += 1
        elif "--" in s:
            count -= 1
    print(count)


if __name__ == '__main__':
    func()
