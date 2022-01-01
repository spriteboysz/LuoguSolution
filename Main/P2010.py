#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-15 22:26:09
LastEditTime: 2021-12-15 22:52:10
Description: 回文日期
FilePath: P2010.py
'''


def func():
    start = input().strip()
    end = input().strip()
    count = 0
    for year in range(int(start[:4]), int(end[:4]) + 2):
        month, day = int(str(year)[::-1][:2]), int(str(year)[::-1][2:])
        if (month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31) or \
            (month in [4, 6, 9, 11] and 1 <= day <= 30) or \
                (month == 2 and 1 <= day <= 29):
            date = year * 10000 + month * 100 + day
            if int(start) <= date <= int(end):
                count += 1
    print(count)


if __name__ == '__main__':
    func()
