#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-02 23:15:30
LastEditTime: 2021-12-02 23:23:11
Description: Phone Code
FilePath: CF172A.py
'''


def func():
    n = int(input())
    phone = []
    for _ in range(n):
        phone.append(list(input().strip()))
    count = 0
    for item in list(zip(*phone)):
        if len(set(item)) == 1:
            count += 1
        else:
            break
    print(count)


if __name__ == '__main__':
    func()
