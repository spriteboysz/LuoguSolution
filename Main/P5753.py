#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-23 21:20:00
LastEditTime: 2021-10-23 21:44:05
Description: 瓷片项链
FilePath: P5753.py
'''


def func():
    v = int(input())
    v0 = int(input())

    num = 1
    lengths = [0]
    while v / num - v0 > 0:
        length = ((v / num - v0) ** 0.5) * 0.3 * num
        lengths.append(length)
        num += 1

    max_length = max(lengths)
    if lengths.count(max_length) > 1:
        print(0)
    else:
        print(lengths.index(max_length))


if __name__ == '__main__':
    func()
    