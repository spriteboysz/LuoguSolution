#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-25 15:57:30
LastEditTime: 2021-09-25 21:33:27
Description: 月份天数
FilePath: P5716.py
'''


def isLeapYear(year):
    if year % 100 == 0 and year % 400 != 0:
        return False
    else:
        return year % 4 == 0


def func():
    year, month = map(int, input().strip().split())
    if month == 2:
        days = 29 if isLeapYear(year) else 28
        print(days)
    elif month in [4, 6, 9, 11]:
        print(30)
    else:
        print(31)


if __name__ == '__main__':
    func()

