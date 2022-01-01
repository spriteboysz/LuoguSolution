#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-16 23:50:40
Description: 奥运奖牌计数
FilePath: B2058.py
'''


def func():
    n = int(input())
    gold, sliver, bronze, total = 0, 0, 0, 0
    for _ in range(n):
        row = list(map(int, input().strip().split()))
        gold += row[0]
        sliver += row[1]
        bronze += row[2]
    total = gold + sliver + bronze
    print(gold, sliver, bronze, total)


if __name__ == '__main__':
    func()
