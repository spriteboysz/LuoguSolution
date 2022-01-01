#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-11 23:05:33
LastEditTime: 2021-11-11 23:06:56
Description: 
FilePath: CF1303A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        s = input().strip("0")
        print(len(s) - s.count("1"))


if __name__ == '__main__':
    func()
