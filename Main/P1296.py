#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 09:36:40
LastEditTime: 2021-10-22 09:46:38
Description: 奶牛的耳语
FilePath: P1296.py
'''


def func():
    n, d = map(int, input().strip().split())
    p = sorted(list(map(int, input().strip().split())))

    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if p[j] - p[i] <= d:
                count += 1
            else:
                break
    print(count)


if __name__ == '__main__':
    func()
