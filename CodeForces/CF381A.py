#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 00:03:51
LastEditTime: 2021-11-27 00:01:35
Description: Sereja and Dima
FilePath: CF381A.py
'''


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))
    lst2 = []
    left, right = 0, n - 1
    while left <= right:
        if lst[left] > lst[right]:
            max = left
            left += 1
        else:
            max = right
            right -= 1
        lst2.append(lst[max])
        
    print(sum(lst2[0::2]), sum(lst2[1::2]))


if __name__ == '__main__':
    func()
