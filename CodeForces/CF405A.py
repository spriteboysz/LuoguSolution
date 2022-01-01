#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-04 23:46:50
LastEditTime: 2021-11-04 23:49:26
Description: Gravity Flip
FilePath: CF405A.py
'''


def func():
    n = int(input())
    boxes = sorted(map(int, input().strip().split()))
    print(" ".join(map(str, boxes)))


if __name__ == '__main__':
    func()
