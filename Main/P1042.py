#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-27 23:25:26
LastEditTime: 2021-12-27 23:48:57
Description: 乒乓球
FilePath: P1042.py
'''


def func():
    record = ""
    while True:
        s = input().strip()
        record += s
        if "E" in s:
            break
    a, b = 0, 0
    for item in record[:(record.index("E") + 1)]:
        if item == "W":
            a += 1
        if item == "L":
            b += 1
        if (a >= 11 or b >= 11) and abs(a - b) > 1 or item == "E":
            print("%s:%s" % (a, b))
            a, b = 0, 0
    print()
    for item in record[:(record.index("E") + 1)]:
        if item == "W":
            a += 1
        if item == "L":
            b += 1
        if (a >= 21 or b >= 21) and abs(a - b) > 1 or item == "E":
            print("%s:%s" % (a, b))
            a, b = 0, 0


if __name__ == '__main__':
    func()
