#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-19 00:09:30
Description: 统计数字字符个数
FilePath: B2109.py
'''


def func():
    s = input().strip()
    count = 0
    for item in s:
        if item in list(map(str, range(10))):
            count += 1
    print(count)


if __name__ == '__main__':
    func()
