#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 14:45:39
Description: 与指定数字相同的数的个数
FilePath: B2087.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    m = int(input())

    count = 0
    for i in range(n):
        if lst[i] == m:
            count += 1
    print(count)


if __name__ == '__main__':
    func()
