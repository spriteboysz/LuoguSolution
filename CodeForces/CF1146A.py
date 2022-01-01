#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-16 23:32:25
LastEditTime: 2021-11-16 23:36:05
Description: Love A
FilePath: CF1146A.py
'''


def func():
    s = input().strip()
    print(min(len(s), s.count("a") * 2 - 1))


if __name__ == '__main__':
    func()
    