#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-01 23:44:52
LastEditTime: 2022-01-01 23:58:48
Description: OKTALNI
FilePath: P6353.py
'''


def func():
    base = {"000": "0", "001": "1", "010": "2", "011": "3",
            "100": "4", "101": "5", "110": "6", "111": "7"}
    s = input().strip()
    if len(s) % 3 != 0:
        s = "0" * (3 - len(s) % 3) + s
    octal = ""
    for i in range(0, len(s), 3):
        octal += base[s[i:i+3]]
    print(octal)


if __name__ == '__main__':
    func()
