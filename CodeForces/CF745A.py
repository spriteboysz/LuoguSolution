#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-30 23:09:49
LastEditTime: 2021-11-30 23:14:40
Description: Hongcow Learns the Cyclic Shift
FilePath: CF745A.py
'''


def func():
    s = input().strip()
    n = len(s)
    s += s
    word = []
    for i in range(n):
        word.append(s[i:i + n])
    print(len(set(word)))


if __name__ == '__main__':
    func()
