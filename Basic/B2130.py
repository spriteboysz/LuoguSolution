#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 00:15:01
LastEditTime: 2021-10-22 09:16:21
Description: 简单算术表达式求值
FilePath: B2130.py
'''


def func():
    expression = input().strip()
    symbols = ["+", "-", "*", "/", "%"]
    for s in symbols:
        if s in expression:
            a, b = map(int, expression.split(s))
            break
    if s == "+":
        print(a + b)
    if s == "-":
        print(a - b)
    if s == "*":
        print(a * b)
    if s == "/":
        print(a // b)
    if s == "%":
        print(a % b)


if __name__ == '__main__':
    func()
