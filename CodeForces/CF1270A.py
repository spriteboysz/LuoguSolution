#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-17 23:39:08
LastEditTime: 2021-11-17 23:49:05
Description: Card Game
FilePath: CF1270A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        _, _, _ = map(int, input().strip().split())
        hs = list(map(int, input().strip().split()))
        zh = list(map(int, input().strip().split()))
        if max(hs + zh) in hs:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    func()
