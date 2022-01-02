#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-02 23:08:24
LastEditTime: 2022-01-02 23:22:20
Description: 危险区域
FilePath: P2074.py
'''


def calcDistance2(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def func():
    n, m, k, t = map(int, input().strip().split())
    count = []
    for _ in range(k):
        x, y = map(int, input().strip().split())
        current = 0
        for i in range(max(1, x - t), min(n, x + t) + 1):
            for j in range(max(1, y - t), min(m, y + t) + 1):
                if calcDistance2(x, y, i, j) <= t * t:
                    current += 1
        count.append(current)
    print(max(count))


if __name__ == '__main__':
    func()
