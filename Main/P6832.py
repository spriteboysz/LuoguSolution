#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 15:43:27
LastEditTime: 2021-10-24 15:50:05
Description: 子弦
FilePath: P6832.py
'''


def func():
    s = input().strip()
    count = 0
    for item in set(s):
        if item != " " and count < s.count(item):
            count = s.count(item)
    print(count)


if __name__ == '__main__':
    func()
