#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-29 23:17:57
LastEditTime: 2021-12-04 22:40:18
Description: Free Cash
FilePath: CF237A.py
'''


def func():
    n = int(input())
    times = [0] * 1500
    for _ in range(n):
        hour, minute = map(int, input().strip().split())
        times[hour * 60 + minute] += 1
    print(max(times))


if __name__ == '__main__':
    func()
