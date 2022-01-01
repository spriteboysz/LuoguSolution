#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-16 23:17:43
LastEditTime: 2021-11-16 23:21:15
Description: Choose Two Numbers
FilePath: CF1206A.py
'''


def func():
    _, a = int(input()), list(map(int, input().strip().split()))
    _, b = int(input()), list(map(int, input().strip().split()))
    print(max(a), max(b))


if __name__ == '__main__':
    func()
