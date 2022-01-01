#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 22:37:35
LastEditTime: 2021-11-07 22:41:31
Description: Arpa’s hard exam and Mehrdad’s naive cheat
FilePath: CF742A.py
'''


def func():
    n = int(input())
    if n == 0:
        print(1)
    else:
        power = [6, 8, 4, 2]
        print(power[n % 4])


if __name__ == '__main__':
    func()
