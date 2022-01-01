#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-26 23:24:20
LastEditTime: 2021-10-26 23:34:05
Description: Olivander
FilePath: P4613.py
'''


def func():
    n = int(input())
    sticks = sorted(map(int, input().strip().split()))
    boxes = sorted(map(int, input().strip().split()))
    # TODO: map函数可以跟两个可迭代对象
    # TODO： all() 所有值为True，结果为True
    if all(map(lambda s, b: s <= b, sticks, boxes)):
        print("DA")
    else:
        print("NE")


if __name__ == '__main__':
    func()
