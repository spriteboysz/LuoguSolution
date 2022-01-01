#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-23 22:55:10
LastEditTime: 2021-12-23 23:07:25
Description: B进制星球
FilePath: P1604.py
'''


from string import ascii_uppercase


def func():
    base = ["0", "1", "2", "3", "4", "5", "6",
            "7", "8", "9"] + list(ascii_uppercase)
    b = int(input())
    num1, num2 = input().strip(), input().strip()
    if len(num1) < len(num2):
        num1, num2 = num2, num1
    num2 = "0" * (len(num1) - len(num2)) + num2

    carry = 0
    num3 = ""
    for i in range(len(num1) - 1, -1, -1):
        carry, mod = divmod(base.index(
            num1[i]) + base.index(num2[i]) + carry, b)
        num3 = str(base[mod]) + num3

    if carry != 0:
        print((str(carry) + num3))
    else:
        print(num3)


if __name__ == '__main__':
    func()
