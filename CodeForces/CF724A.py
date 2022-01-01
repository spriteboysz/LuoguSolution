#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-14 17:23:30
LastEditTime: 2021-11-14 17:39:24
Description: Checking the Calendar
FilePath: CF724A.py
'''


def func():
    week = ["monday", "tuesday", "wednesday",
            "thursday", "friday", "saturday", "sunday"]

    a, b = input().strip(), input().strip()
    if a == b and a in week:
        print("YES")
    elif week[(week.index(a) + 2) % 7] == b:
        print("YES")
    elif week[(week.index(a) + 3) % 7] == b:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
