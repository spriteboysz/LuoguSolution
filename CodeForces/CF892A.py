#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 23:08:06
LastEditTime: 2021-11-19 23:17:29
Description: Greed
FilePath: CF892A.py
'''


def func():
    _ = int(input())
    remaining = sum(map(int, input().strip().split()))
    cans = list(map(int, input().strip().split()))
    first = max(cans)
    cans.remove(first)
    second = max(cans)
    print("YES" if first + second >= remaining else "NO")


if __name__ == '__main__':
    func()
