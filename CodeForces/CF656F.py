#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-06 23:31:38
LastEditTime: 2021-11-06 23:35:18
Description: Ace It!
FilePath: CF656F.py
'''


def func():
    s = list(input().strip())
    count = 0
    for item in s:
        if item == "A":
            count += 1
        elif item == "1":
            count += 10
        else:
            count += int(item)
    print(count)


if __name__ == '__main__':
    func()
