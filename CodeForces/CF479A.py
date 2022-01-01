#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-01 21:43:20
LastEditTime: 2021-12-01 21:46:32
Description: Expression
FilePath: CF479A.py
'''


def func():
    a, b, c = int(input()), int(input()), int(input())
    expression = []
    expression.append(a + b + c)
    expression.append(a + b * c)
    expression.append(a * b + c)
    expression.append(a * b * c)
    expression.append((a + b) * c)
    expression.append(a * (b + c))
    print(max(expression))


if __name__ == '__main__':
    func()
