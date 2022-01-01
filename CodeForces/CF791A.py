#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-22 23:54:02
LastEditTime: 2021-11-22 23:57:50
Description: Bear and Big Brother
FilePath: CF791A.py
'''


def func():
    a, b = map(int, input().strip().split())
    count = 0
    while(a <= b):
        a, b = a * 3, b * 2
        count += 1
    print(count)


if __name__ == '__main__':
    func()
    