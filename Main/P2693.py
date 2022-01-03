#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-03 22:14:32
LastEditTime: 2022-01-03 22:41:12
Description: 号码锁 Combination Lock
FilePath: P2693.py
'''


def func():
    n = int(input())
    x, y, z = map(int, input().strip().split())
    a, b, c = map(int, input().strip().split())
    if n < 5:
        print(n ** 3)
    else:
        bo1, bo2 = [], []
        for i in range(-2, 3):
            for j in range(-2, 3):
                for k in range(-2, 3):
                    bo1.append(((x + i + n) % n, (y + j + n) %
                               n, (z + k + n) % n))
                    bo2.append(((a + i + n) % n, (b + j + n) %
                               n, (c + k + n) % n))
        print(5 ** 3 * 2 - len(set(bo1) & set(bo2)))


if __name__ == '__main__':
    func()
