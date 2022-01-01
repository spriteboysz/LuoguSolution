#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-20 23:11:17
LastEditTime: 2021-10-20 23:24:28
Description: 字符串P型编码
FilePath: B2123.py
'''


def func():
    s1 = input().strip()
    s2 = [1] * len(s1)
    for i in range(1, len(s1)):
        if s1[i] == s1[i - 1]:
            s2[i] = s2[i - 1] + 1
            s2[i - 1] = 0
    p = ""
    for i, j in zip(s1, s2):
        if j != 0:
            p += str(j) + i
    print(p)


if __name__ == '__main__':
    func()
