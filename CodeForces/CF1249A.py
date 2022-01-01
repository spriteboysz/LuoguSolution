#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-17 23:51:12
LastEditTime: 2021-11-17 23:54:01
Description: Yet Another Dividing into Teams
FilePath: CF1249A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(sorted(map(int, input().strip().split())))
        for i in range(0, n - 1):
            if lst[i + 1] - lst[i] == 1:
                print(2)
                break
        else:
            print(1)


if __name__ == '__main__':
    func()
