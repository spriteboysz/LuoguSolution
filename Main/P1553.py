#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-13 23:21:13
LastEditTime: 2021-10-14 00:00:23
Description: 数字反转（升级版）
FilePath: P1553.py
'''


def reverse(s, ch):
    s1, s2 = map(str, map(int, s.split(ch)))
    return str(int(s1[::-1])) + ch + str(int(s2[::-1]))


def func():
    s = input().strip()

    if "." in s:
        s = reverse(s, ".")
    elif "/" in s:
        s = reverse(s, "/")
    elif "%" in s:
        s = reverse(s + "0", "%")
        s = s[:-1]
    else:
        s = int(s[::-1])

    print(s)


if __name__ == '__main__':
    func()
