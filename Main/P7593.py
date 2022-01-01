#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-14 22:46:50
LastEditTime: 2021-12-14 22:52:27
Description: 凑数
FilePath: P7593.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n, k, s = map(int, input().strip().split())
        minimum = k * (k + 1) // 2
        maximun = ((2 * n + 1) * k - k * k) // 2
        if minimum <= s <= maximun:
            print("Yes")
        else:
            print("No")


if __name__ == '__main__':
    func()
