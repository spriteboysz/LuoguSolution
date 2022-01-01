#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-03 21:31:17
LastEditTime: 2021-12-03 21:39:50
Description: Lucky Ticket
FilePath: CF146A.py
'''


def func():
    n = int(input())
    num = list(map(int, list(input().strip())))
    if num.count(4) + num.count(7) == n and sum(num[:(n//2)]) == sum(num[(n//2):]):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
