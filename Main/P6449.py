#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-25 23:32:36
LastEditTime: 2021-12-25 23:46:57
Description: B
FilePath: P6449.py
'''


def func():
    d, m = map(int, input().strip().split())
    month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    week = ["Wednesday", "Thursday", "Friday",
            "Saturday", "Sunday", "Monday", "Tuesday"]
    days = d
    for i in range(m):
        days += month[i]
    print(week[days % 7])


if __name__ == '__main__':
    func()
