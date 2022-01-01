#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 23:09:44
LastEditTime: 2021-11-21 17:28:01
Description: New Year and Hurry
FilePath: CF750A.py
'''


def func():
    n, k = map(int, input().strip().split())
    time = 0
    for i in range(1, n + 1):
        time += i * 5
        if time + k > 4 * 60:
            print(i - 1)
            break
    else:
        print(n)


if __name__ == '__main__':
    func()