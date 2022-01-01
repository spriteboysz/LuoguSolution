#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-23 22:50:25
LastEditTime: 2021-11-23 22:56:49
Description: Common Subsequence
FilePath: CF1382A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().strip().split())
        lst1 = set(map(int, input().strip().split()))
        lst2 = set(map(int, input().strip().split()))
        if len(lst1 & lst2) != 0:
            print("YES")
            print("1 " + str(list(lst1 & lst2)[0]))
        else:
            print("NO")


if __name__ == '__main__':
    func()
