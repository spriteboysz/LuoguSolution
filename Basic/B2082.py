#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-26 22:34:28
LastEditTime: 2021-09-26 22:39:21
Description: 数字统计
FilePath: B2082.py
'''


def func():
    l, r = map(int, input().strip().split())
    lst = []
    for i in range(l, r + 1):
        lst.append(str(i))

    print("".join(lst).count("2"))


if __name__ == '__main__':
    func()
