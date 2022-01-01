#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-09-26 22:10:32
LastEditTime: 2021-09-26 22:16:15
Description: 大象喝水
FilePath: B2029.py
'''


def func():
    h, r = map(int, input().strip().split())
    pi = 3.14159

    print(int(20 * 1000 // (pi * r * r * h) + 1))


if __name__ == '__main__':
    func()
