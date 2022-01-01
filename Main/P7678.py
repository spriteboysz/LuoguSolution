#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-14 23:51:17
LastEditTime: 2021-12-14 23:54:33
Description: LJESNJAK
FilePath: P7678.py
'''


def func():
    s = input().strip()
    for el in ["dz=", "c=", "c-", "d-", "lj", "nj", "s=", "z="]:
        s = s.replace(el, "+")
    print(len(s))


if __name__ == '__main__':
    func()
