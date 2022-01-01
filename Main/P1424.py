#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-06 22:04:50
Description: 小鱼的航程（改进版）
FilePath: P1424.py
'''


def func():
    week, days = map(int, input().strip().split())

    count = 0
    for i in range(1, days + 1):
        if week != 6 and week != 7:
            count += 1
        week = 1 if week == 7 else week + 1

    print(250 * count)


if __name__ == '__main__':
    func()
