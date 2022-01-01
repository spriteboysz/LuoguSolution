#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-15 23:22:51
LastEditTime: 2021-12-15 23:26:02
Description: Bridž
FilePath: P7533.py
'''


def func():
    base = ["X", "J", "Q", "K", "A"]
    n = int(input())
    total = 0
    for _ in range(n):
        cards = input().strip()
        for el in cards:
            total += base.index(el)
            
    print(total)


if __name__ == '__main__':
    func()
