#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-21 22:58:48
LastEditTime: 2021-12-21 23:03:58
Description: 不高兴的津津（升级版）
FilePath: P1534.py
'''


def func():
    n = int(input())
    total, unhappy = 0, 0
    for _ in range(n):
        a, b = map(int, input().strip().split())
        unhappy += a + b - 8
        total += unhappy
    print(total)


if __name__ == '__main__':
    func()
