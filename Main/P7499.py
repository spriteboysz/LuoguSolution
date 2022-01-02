#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-02 17:54:18
LastEditTime: 2022-01-02 17:57:03
Description: 概率
FilePath: P7499.py
'''


def func():
    t = int(input())
    for _ in range(t):
        a, b, c, d, e = map(int, input().strip().split())
        print(max(0, min(e - a, d) - max(e - b, c) + 1))


if __name__ == '__main__':
    func()
