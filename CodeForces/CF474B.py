#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 16:03:00
LastEditTime: 2021-11-21 16:20:43
Description: Worms
FilePath: CF474B.py
'''


def func():
    n = int(input())
    worms = list(map(int, input().strip().split()))
    m = int(input())
    juicy = list(map(int, input().strip().split()))
    for i in range(1, n):
        worms[i] += worms[i - 1]

    for i in range(m):
        for j in range(n):
            if juicy[i] <= worms[j]:
                print(j + 1)
                break


if __name__ == '__main__':
    func()
