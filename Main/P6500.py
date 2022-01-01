#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 16:35:05
LastEditTime: 2021-10-24 16:44:25
Description: ZBROJ
FilePath: P6500.py
'''


def func():
    s = input().strip()
    maximum = sum(map(int, s.replace("6", "5").split()))
    minium = sum(map(int, s.replace("5", "6").split()))

    print(maximum, minium)
    


if __name__ == '__main__':
    func()
    