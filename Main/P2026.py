#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-18 14:15:02
LastEditTime: 2021-12-19 17:43:51
Description: 求一次函数解析式
FilePath: P2026.py
'''


from math import gcd


def func():
    x1, y1 = map(int, input().strip().split())
    x2, y2 = map(int, input().strip().split())
    s = "y="
    if x1 == x2:
        print("x=" + str(x1))
    else:
        a1, a2 = (y1 - y2), (x1 - x2)
        b1, b2 = (y2 * x1 - y1 * x2), (x1 - x2)
        if a1 * a2 < 0:
            s += "-"
        if abs(a1) == abs(a2):
            s += "x"
        elif a1 % a2 == 0:
            s += str(abs(a1 // a2)) + "x"
        else:
            s += str(abs(a1 // gcd(a1, a2))) + "/" + \
                str(abs(a2 // gcd(a1, a2))) + "*x"
        if b1 == 0:
            print(s)
            return
        elif b1 * b2 < 0:
            s += "-"
        else:
            s += "+"
        if b1 % b2 == 0:
            s += str(abs(b1 // b2))
        else:
            s += str(abs(b1 // gcd(b1, b2))) + "/" + \
                str(abs(b2 // gcd(b1, b2)))
        print(s)


if __name__ == '__main__':
    func()