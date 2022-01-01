#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-06 15:02:06
LastEditTime: 2021-11-06 15:12:56
Description: Keyboard
FilePath: CF474A.py
'''


def func():
    direct = input().strip()
    s1 = input().strip()
    base1 = "qwertyuiopasdfghjkl;zxcvbnm,./"
    if direct == "R":
        base2 = base1[-1] + base1[:-1]
    elif direct == "L":
        base2 = base1[1:] + base1[0]

    s2 = ""
    for item in s1:
        s2 += base2[base1.index(item)]
    print(s2)


if __name__ == '__main__':
    func()
