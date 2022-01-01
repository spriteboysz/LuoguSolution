#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 14:10:05
LastEditTime: 2021-11-26 14:17:58
Description: Hamster Farm
FilePath: CF939B.py
'''


def func():
    n, k = map(int, input().strip().split())
    boxes = list(map(int, input().strip().split()))
    minimum = n
    index, number = 0, 0
    for i in range(k):
        div, mod = divmod(n, boxes[i])
        if mod < minimum:
            minimum = mod
            index, number = i, div
    print(index + 1, number)


if __name__ == '__main__':
    func()
