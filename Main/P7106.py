#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-09 23:31:13
LastEditTime: 2021-12-09 23:36:29
Description: 双生独白
FilePath: P7106.py
'''


def func():
    base = ["0", "1", "2", "3", "4", "5", "6", "7",
            "8", "9", "A", "B", "C", "D", "E", "F"]
    color = input().strip()
    reverse = ""
    for item in color:
        if item == "#":
            reverse += item
        else:
            reverse += base[15 - base.index(item)]
    print(reverse)


if __name__ == '__main__':
    func()
