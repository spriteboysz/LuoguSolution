#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-01 23:14:16
LastEditTime: 2021-12-01 23:17:31
Description: Second-Price Auction
FilePath: CF386A.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    ans1 = lst.index(max(lst)) + 1
    lst.remove(max(lst))
    ans2 = max(lst)
    print(ans1, ans2)


if __name__ == '__main__':
    func()
