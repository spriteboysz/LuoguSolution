#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 16:17:55
Description: 不与最大数相同的数字之和
FilePath: B2094.py
'''


def func():
    n = int(input())
    # !需增加判断n为0的情况
    if n == 0:
        print(0)
    else: 
        lst = list(map(int, input().strip().split()))   
        count = 0
        for i in range(n):
            if lst[i] != max(lst):
                count += lst[i]

        print(count)


if __name__ == '__main__':
    func()
