#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-25 23:22:14
LastEditTime: 2021-11-25 23:25:01
Description: Arena
FilePath: CF1487A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        heroes = list(map(int, input().strip().split()))
        print(len(heroes) - heroes.count(min(heroes)))


if __name__ == '__main__':
    func()
