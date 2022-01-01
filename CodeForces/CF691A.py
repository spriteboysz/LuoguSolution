#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 16:18:22
LastEditTime: 2021-11-07 16:33:05
Description: Fashion in Berland
FilePath: CF691A.py
'''


def func():
    n = int(input())
    buttons = list(map(int, input().strip().split()))
    # *第一个if条件的否定分支中要考虑 n == 1 and sum(buttons) != 1
    if n == 1 and sum(buttons) == 1:
        print("YES")
    elif n != 1 and sum(buttons) == n - 1:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
