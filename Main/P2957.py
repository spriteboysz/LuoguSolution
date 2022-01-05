#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-05 22:49:34
LastEditTime: 2022-01-05 23:05:52
Description: [USACO09OCT]Barn Echoes G
FilePath: P2957.py
'''


def func():
    a, b = input().strip(), input().strip()
    if len(a) > len(b):
        a, b = b, a

    count1, count2 = 0, 0
    for i in range(len(a) - 1):
        if b.endswith(a[:len(a) - i - 1]):
            count1 = len(a) - i - 1
            break
    for i in range(len(a) - 1):
        if b.startswith(a[i:]):
            count2 = len(a) - i
            break
    print(max(count1, count2))


if __name__ == '__main__':
    func()
