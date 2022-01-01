#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-29 22:45:18
LastEditTime: 2021-12-29 22:55:36
Description: 火星上的加法运算
FilePath: P1952.py
'''


from string import ascii_lowercase, digits


def func():
    base = list(digits + ascii_lowercase)
    b = int(input())
    num1, num2 = input().strip(), input().strip()
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    num2 = "0" * (len(num1) - len(num2)) + num2

    carry, num3 = 0, ""
    for i in range(len(num1) - 1, -1, -1):
        carry, mod = divmod(base.index(
            num1[i]) + base.index(num2[i]) + carry, b)
        num3 = str(base[mod]) + num3

    print(str(carry) + num3 if carry != 0 else num3)


if __name__ == '__main__':
    func()
