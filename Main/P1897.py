#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 21:27:43
LastEditTime: 2021-10-22 21:36:25
Description: 电梯里的爱情
FilePath: P1897.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))

    time = max(lst) * (6 + 4) + len(set(lst)) * 5 + n
    print(time)


if __name__ == '__main__':
    func()
