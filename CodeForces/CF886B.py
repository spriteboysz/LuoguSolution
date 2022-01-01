#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-13 22:41:02
LastEditTime: 2021-12-03 23:43:54
Description: Vlad and Cafes
FilePath: CF886B.py
'''


def func():
    n = int(input())
    lst1 = list(map(int, input().strip().split()))
    lst2 = [0] * 200005
    for i in range(n - 1, -1, -1):
        if lst2[lst1[i]] != 1:
            ans = lst1[i]
        lst2[lst1[i]] = 1
    print(ans)


if __name__ == '__main__':
    func()
