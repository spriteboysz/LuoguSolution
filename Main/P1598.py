#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-06 22:44:43
LastEditTime: 2021-12-06 23:01:48
Description: 垂直柱状图
FilePath: P1598.py
'''

from string import ascii_uppercase


def func():
    s = ""
    for _ in range(4):
        s += input().strip()
    alphabet = [0] * 26
    for item in s:
        if item.isupper():
            alphabet[ord(item) - ord("A")] += 1

    for i in range(max(alphabet), 0, -1):
        row = ""
        for j in range(len(alphabet)):
            if alphabet[j] >= i:
                row += "* "
            else:
                row += "  "
        print(row.rstrip())
    print(" ".join(list(ascii_uppercase)))


if __name__ == '__main__':
    func()
