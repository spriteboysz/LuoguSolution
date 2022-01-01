#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-22 23:44:08
LastEditTime: 2021-11-22 23:47:33
Description: Nearly Lucky Number
FilePath: CF110A.py
'''


def func():
    num = input().strip()
    count = 0
    for item in num:
        if item == "4" or item == "7":
            count += 1
    lucy = str(count).replace("4", "").replace("7", "")
    print("YES" if len(lucy) == 0 else "NO")


if __name__ == '__main__':
    func()
