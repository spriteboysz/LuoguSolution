#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-30 23:33:21
LastEditTime: 2021-11-30 23:34:38
Description: Case of the Zeros and Ones
FilePath: CF556A.py
'''


def func():
    n = int(input())
    num = input().strip()
    print(abs(num.count("1") - num.count("0")))


if __name__ == '__main__':
    func()
