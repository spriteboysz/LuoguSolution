#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 23:18:48
Description: 打分
FilePath: P5726.py
'''

def func():
    n = int(input())
    lst = list(map(float, input().strip().split()))

    print("%.2f" % ((sum(lst) - max(lst) - min(lst)) / (n - 2)))


if __name__ == '__main__':
    func()
    