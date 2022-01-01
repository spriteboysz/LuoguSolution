#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-25 23:01:14
LastEditTime: 2021-12-25 23:10:09
Description: BUKA
FilePath: P6467.py
'''


def func():
    a, operator, b = input().strip(), input().strip(), input().strip()
    if operator == "*":
        print("1" + "0" * (len(a) + len(b) - 2))
    elif operator == "+":
        if len(a) > len(b):
            print("1" + "0" * (len(a) - len(b) - 1) + b)
        elif len(a) < len(b):
            print("1" + "0" * (len(b) - len(a) - 1) + a)
        else:
            print("2" + "0" * (len(a) - 1))


if __name__ == '__main__':
    func()
