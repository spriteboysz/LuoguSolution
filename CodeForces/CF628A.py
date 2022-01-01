#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 16:47:36
LastEditTime: 2021-11-21 16:54:59
Description: Tennis Tournament
FilePath: CF628A.py
'''


def func():
    # * n个人比赛，每次比赛淘汰一人，最后仅剩下一人，一共进行n-1次比赛
    #！ 中文注释会报编译错误
    n, b, p = map(int, input().strip().split())
    print((2 * b + 1) * (n - 1), p * n)


if __name__ == '__main__':
    func()
