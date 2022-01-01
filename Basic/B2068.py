#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 22:20:40
Description: 统计满足条件的4位数
FilePath: B2068.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))

    count = 0
    for item in lst:
        a, b, c, d = map(int, list(str(item)))
        if d - a - b - c > 0:
            count += 1

    print(count)
    


if __name__ == '__main__':
    func()
