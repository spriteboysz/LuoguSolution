#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 17:22:40
LastEditTime: 2021-11-21 17:49:43
Description: Juicer
FilePath: CF709A.py
'''


def func():
    n, b, d = map(int, input().strip().split())
    lst = list(map(int, input().strip().split()))
    count = 0
    size = 0
    for i in range(n):
        if lst[i] <= b:
            size += lst[i]
            if size > d:
                count += 1
                size = 0
    print(count)
            

if __name__ == '__main__':
    func()
    