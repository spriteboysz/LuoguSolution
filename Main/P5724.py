#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 22:39:16
Description: 求极差 / 最大跨度值
FilePath: P5724.py
'''
def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    print(max(lst) - min(lst))

if __name__ == '__main__':
    func()
    