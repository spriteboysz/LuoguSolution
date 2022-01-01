#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-20 22:31:11
LastEditTime: 2021-10-20 22:52:53
Description: 加密的病历单
FilePath: B2116.py
'''

import string


def func():
    s1 = input().strip()

    mapping1 = string.ascii_lowercase
    mapping2 = string.ascii_uppercase
    mapping1 = mapping1[3:] + mapping1[:3]
    mapping2 = mapping2[3:] + mapping2[:3]
    s2 = ""
    for item in s1:
        if item.islower():
            item = mapping1[string.ascii_lowercase.index(item)]
            s2 += item.upper()
        else:
            item = mapping2[string.ascii_uppercase.index(item)]
            s2 += item.lower()
    print("".join(reversed(s2)))


if __name__ == '__main__':
    func()
