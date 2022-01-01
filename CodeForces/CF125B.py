#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 23:17:34
LastEditTime: 2021-11-28 23:28:43
Description: Simple XML
FilePath: CF125B.py
'''


def func():
    label = input().strip().lstrip("<").rstrip(">").split("><")
    high = []
    h = 0
    for item in label:
        if "/" not in item:
            high.append(h)
            h += 1
    print(label)
    print(high)
    


if __name__ == '__main__':
    func()
    