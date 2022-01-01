#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-25 23:42:33
LastEditTime: 2021-11-25 23:46:02
Description: Sasha and Stick
FilePath: CF832A.py
'''


def func():
    n, k = map(int, input().strip().split())
    if (n // k) % 2 != 0:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
