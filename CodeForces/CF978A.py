#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-25 23:55:50
LastEditTime: 2021-11-26 00:11:16
Description: Remove Duplicates
FilePath: CF978A.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    for i in range(n - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if lst[j] == lst[i]:
                lst.pop(j)
                break
            
    print(len(lst))
    print(" ".join(map(str, lst)))


if __name__ == '__main__':
    func()
