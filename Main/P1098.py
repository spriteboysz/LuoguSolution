#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-08 23:18:25
LastEditTime: 2022-01-09 00:12:04
Description: [NOIP2007 提高组] 字符串的展开
FilePath: P1098.py
'''

from string import ascii_lowercase


def func():
    base = ascii_lowercase + "0123456789"
    p1, p2, p3 = map(int, input().strip().split())
    s1 = input().strip()
    s2 = ""
    for i, v in enumerate(s1):
        if v == "-":
            if i == 0 or i == len(s1) - 1 or s1[i - 1] >= s1[i + 1]:
                s2 += v
            elif s1[i - 1].isdigit() and s1[i + 1].isdigit() or s1[i - 1].islower() and s1[i + 1].islower():
                temp = ""
                for i in range(base.index(s1[i - 1]) + 1, base.index(s1[i + 1])):
                    temp += base[i] * p2
                if p1 == 2:
                    temp = temp.upper()
                elif p1 == 3:
                    temp = "*" * len(temp)
                if p3 == 2:
                    temp = temp[::-1]
                s2 += temp
            else:
                s2 += v
        else:
            s2 += v
    print(s2)


if __name__ == '__main__':
    func()
