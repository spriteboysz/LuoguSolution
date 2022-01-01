#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-25 23:56:41
LastEditTime: 2021-10-26 00:01:05
Description: 加减算式
FilePath: P2788.py
'''


def func():
    expression = input().strip()
    lst = list(map(int, expression.replace("-", "+-").split("+")))
    print(sum(lst))


if __name__ == '__main__':
    func()
