#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-22 23:09:57
LastEditTime: 2021-11-22 23:16:56
Description: A Serial Killer
FilePath: CF776A.py
'''


def func():
    lst = input().strip().split()
    n = int(input())
    print(" ".join(lst))
    for _ in range(n):
        old, new = input().strip().split()
        lst.remove(old)
        lst.append(new)
        print(" ".join(lst))


if __name__ == '__main__':
    func()
