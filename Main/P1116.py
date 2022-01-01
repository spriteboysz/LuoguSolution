#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 10:38:21
LastEditTime: 2021-12-08 23:35:00
Description: 车厢重组
FilePath: P1116.py
'''


def func():
    n = int(input())
    lst = []
    length = len(lst)
    while length < n:
        lst.extend(list(map(int, input().strip().split())))
        length = len(lst)

    count = 0
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if lst[j] > lst[j + 1]:
                count += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print(count)


if __name__ == '__main__':
    func()
