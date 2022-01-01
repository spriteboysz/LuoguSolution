#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 16:46:24
LastEditTime: 2021-10-24 16:49:57
Description: OKUPLJANJE
FilePath: P6488.py
'''


def func():
    l, p = map(int, input().strip().split())
    lst = list(map(int, input().strip().split()))

    for i in range(len(lst)):
        lst[i] -= l * p
    print(" ".join(map(str, lst)))

if __name__ == '__main__':
    func()
    