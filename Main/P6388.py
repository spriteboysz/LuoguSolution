#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-04 23:19:08
LastEditTime: 2022-01-04 23:39:07
Description: [COCI2007-2008#4] LEKTIRA
FilePath: P6388.py
'''


def func():
    s = input().strip()
    index1 = s.index(min(s[:-2]))
    s1 = s[:index1 + 1][::-1]
    s = s[index1 + 1:]
    index2 = s.index(min(s[:-1]))
    s2 = s[:index2 + 1][::-1]
    s = s[index2 + 1:]
    s3 = s[::-1]
    print(s1 + s2 + s3)


if __name__ == '__main__':
    func()
