#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-08 23:57:03
LastEditTime: 2021-11-09 00:00:03
Description: Generous Kefa
FilePath: CF841A.py
'''


def func():
    _, k = map(int, input().strip().split())
    s = list(input().strip())
    for item in set(s):
        if s.count(item) > k:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    func()
