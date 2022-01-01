#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-05 17:49:21
LastEditTime: 2021-12-05 21:36:36
Description: 黑蚊子多
FilePath: P5613.py
'''


def func():
    n, m, k = map(int, input().strip().split())
    if k > 0:
        special = list(map(int, input().strip().split()))
    else:
        special = []

    step, time = 0, 0
    while step < n:
        if step in special:
            m += 1
        step += m
        time += 1
    print(time)


if __name__ == '__main__':
    func()
