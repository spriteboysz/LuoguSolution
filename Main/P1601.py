#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-10-16 00:07:02
LastEditTime: 2021-10-16 00:15:24
Description: A+B Problem
FilePath: P1601.py
"""


def func():
    a = input().strip()
    b = input().strip()
    if len(a) < len(b):
        a, b = b, a
    b = "0" * (len(a) - len(b)) + b

    # carry 进位标志
    carry = 0
    c = ""
    for i in range(len(a) - 1, -1, -1):
        carry, mod = divmod(int(a[i]) + int(b[i]) + carry, 10)
        c = str(mod) + c

    print((str(carry) + c) if carry != 0 else c)


if __name__ == "__main__":
    func()
