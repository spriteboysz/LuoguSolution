#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 17:47:35
LastEditTime: 2021-11-28 17:49:34
Description: LLPS
FilePath: CF202A.py
'''


def func():
    s = list(input().strip())
    word = sorted(s)[-1]
    count = s.count(word)
    print(word * count)


if __name__ == '__main__':
    func()
