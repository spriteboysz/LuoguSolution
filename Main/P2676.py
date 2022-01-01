#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-08 22:19:40
LastEditTime: 2021-12-08 22:25:27
Description: Bookshelf B
FilePath: P2676.py
'''


def func():
    n, b = map(int, input().strip().split())
    height = []
    for _ in range(n):
        height.append(int(input()))
    height = sorted(height, reverse=True)
    h = 0
    for i, el in enumerate(height):
        h += el
        if h >= b:
            print(i + 1)
            break
    else:
        print(-1)


if __name__ == '__main__':
    func()
