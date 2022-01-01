#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 22:51:17
LastEditTime: 2021-11-07 22:55:02
Description: 
FilePath: CF784B.py
'''


def func():
    num = hex(int(input())).replace("0x", "").upper()
    count = 0
    for item in num:
        if item in ["0", "4", "6", "9", "A", "D"]:
            count += 1
        elif item in ["8", "B"]:
            count += 2
    print(count)


if __name__ == '__main__':
    func()
