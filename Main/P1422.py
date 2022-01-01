#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-06 22:37:42
Description: 小玉家的电费
FilePath: P1422.py
'''


def func():
    s = int(input())
    count = 0
    for i in range(1, s + 1):
        if i <= 150:
            count += 0.4463
        elif 151 <= i <= 400:
            count += 0.4663
        else:
            count += 0.5663

    print("%.1f" % count)


if __name__ == '__main__':
    func()
