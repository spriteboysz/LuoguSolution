#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 14:41:01
LastEditTime: 2021-11-20 14:51:07
Description: Stone
FilePath: CF1236A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        a, b, c = map(int, input().strip().split())
        stones = 0
        if c / 2 >= b:
            stones += 3 * b
        else:
            b -= c // 2
            stones += c // 2 * 3
            if b / 2 >= a:
                stones += 3 * a
            else:
                stones += b // 2 * 3
        print(stones)


if __name__ == '__main__':
    func()
