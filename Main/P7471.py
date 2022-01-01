#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-15 23:28:09
LastEditTime: 2021-12-15 23:33:07
Description: 切蛋糕
FilePath: P7471.py
'''


def func():
    t = int(input())
    for _ in range(t):
        a, b, c = sorted(map(int, input().strip().split()))
        if a == b == 0:
            print(0)
        elif a == 0:
            print(1 if b == c else 2)
        elif a == b or b == c or a + b == c:
            print(2)
        else:
            print(3)


if __name__ == '__main__':
    func()
