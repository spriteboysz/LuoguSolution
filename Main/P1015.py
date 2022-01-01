#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-27 23:02:49
LastEditTime: 2021-12-27 23:25:02
Description: 回文数
FilePath: P1015.py
'''


from string import ascii_uppercase


def addition(a, b, m):
    base = ["0", "1", "2", "3", "4", "5", "6",
            "7", "8", "9"] + list(ascii_uppercase)
    if len(a) < len(b):
        a, b = b, a
    b = "0" * (len(a) - len(b)) + b

    c, carry = "", 0
    for i in range(len(a) - 1, -1, -1):
        carry, mod = divmod(base.index(
            a[i]) + base.index(b[i]) + carry, m)
        c = str(base[mod]) + c
    return (str(carry) + c) if carry != 0 else c


def func():
    m, n = int(input()), input().strip()
    for i in range(30 + 1):
        if n == n[::-1]:
            print("STEP=%d" % i)
            break
        else:
            n = addition(n, n[::-1], m)
    else:
        print("Impossible!")


if __name__ == '__main__':
    func()
