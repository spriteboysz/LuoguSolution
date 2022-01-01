#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 00:02:48
Description: 鸡尾酒疗法
FilePath: B2065.py
'''


def func():
    n = int(input())
    total, effective = map(int, input().strip().split())
    cocktail = effective / total
    for _ in range(n - 1):
        t, e = map(int, input().strip().split())
        if e / t - cocktail > 0.05:
            print("better")
        elif cocktail - e / t > 0.05:
            print("worse")
        else:
            print("same")


if __name__ == '__main__':
    func()
