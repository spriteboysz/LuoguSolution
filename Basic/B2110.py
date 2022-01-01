#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-19 23:57:00
LastEditTime: 2021-10-20 00:00:37
Description: 找第一个只出现一次的字符
FilePath: B2110.py
'''


def func():
    s = input().strip()
    for item in s:
        if s.count(item) == 1:
            print(item)
            return
    print("no")


if __name__ == '__main__':
    func()
