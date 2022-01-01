#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-15 23:38:29
LastEditTime: 2021-11-15 23:43:37
Description: 
FilePath: CF992A.py
'''


def func():
    _ = int(input())
    lst = list(set(map(int, input().strip().split())) - set([0]))
    print(len(lst))


if __name__ == '__main__':
    func()
