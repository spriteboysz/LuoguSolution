#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 00:03:07
LastEditTime: 2021-11-03 00:05:35
Description: Ultra-Fast Mathematician
FilePath: CF61A.py
'''


def func():
    s1, s2 = input().strip(), input().strip()
    s3 = ""
    for i, j in zip(s1, s2):
        s3 += str(int(i) ^ int(j))
    return s3


if __name__ == '__main__':
    ans = func()
    print(ans)
