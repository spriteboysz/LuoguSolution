#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 00:14:18
LastEditTime: 2021-11-20 13:27:27
Description: Pigeon d'Or 
FilePath: CF1145D.py
'''


def func():
    #*two plus xor of third and min elements
    #*二加上第三个数与最小的数的异或
    n = int(input())
    lst = list(map(int, input().strip().split()))
    print((min(lst) ^ lst[2]) + 2)


if __name__ == '__main__':
    func()
    