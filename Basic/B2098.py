#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 16:39:49
Description: 整数去重
FilePath: B2098.py
'''


def func():
    n = int(input())
    lst = input().strip().split()

    lst2 = []
    for item in lst:
        if item not in lst2:
            lst2.append(item)
    print(" ". join(lst2))

    # for i in range(n - 1):
    #     for j in range(i + 1, n):
    #         if lst[j] == lst[i]:
    #             lst[j] = None

    # lst2 = []
    # for i in range(n):
    #     if lst[i] != None:
    #         lst2.append(lst[i])

    # print(" ".join(lst2))


if __name__ == '__main__':
    func()
