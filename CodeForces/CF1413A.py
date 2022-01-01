#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 23:56:53
LastEditTime: 2021-11-25 00:00:19
Description: Finding Sasuke
FilePath: CF1413A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().strip().split()))
        lst2 = lst[::-1]
        for i in range(len(lst) // 2):
            lst2[i] = - lst2[i]
        print(" ".join(map(str, lst2)))


if __name__ == '__main__':
    func()
