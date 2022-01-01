#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-20 22:51:48
LastEditTime: 2021-12-20 22:55:26
Description: 正方
FilePath: P7042.py
'''


def func():
    q = int(input())
    for _ in range(q):
        a, b, c, d = sorted(map(int, input().strip().split()))
        if a + d != b + c:
            print(0)
        elif a == d:
            print(1)
        elif a == b:
            print(4)
        else:
            print(8)


if __name__ == '__main__':
    func()
