#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-06 23:40:39
LastEditTime: 2022-01-06 23:45:58
Description: [USACO09DEC]Music Notes S
FilePath: P2969.py
'''


def func():
    n, q = map(int, input().strip().split())
    scale = []
    i = 1
    for _ in range(n):
        scale.extend([i] * int(input()))
        i += 1

    for _ in range(q):
        print(scale[int(input())])


if __name__ == '__main__':
    func()
