#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-30 22:52:41
LastEditTime: 2021-11-30 22:54:53
Description: HQ9+
FilePath: CF133A.py
'''


def func():
    s = input().strip()
    for item in s:
        if item in ["H", "Q", "9"]:
            print("YES")
            break
    else:
        print("NO")


if __name__ == '__main__':
    func()
