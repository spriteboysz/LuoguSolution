#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-19 16:44:29
LastEditTime: 2021-12-19 16:53:08
Description: PRASE
FilePath: P6367.py
'''


def func():
    n = int(input())
    lst = []
    count = 0
    for _ in range(n):
        name = input().strip()
        if lst.count(name) * 2 > len(lst):
            count += 1
        lst.append(name)
    print(count)


if __name__ == '__main__':
    func()
