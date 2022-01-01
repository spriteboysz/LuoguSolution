#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-06 14:50:27
Description: ABC
FilePath: P4414.py
'''


def func():
    a, b, c = sorted(list(map(int, input().strip().split())))
    type = input().strip()
    lst = []
    for item in type:
        if item == "A":
            lst.append(str(a))
        elif item == "B":
            lst.append(str(b))
        elif item == "C":
            lst.append(str(c))

    print(" ".join(lst))


if __name__ == '__main__':
    func()
