#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-25 23:13:26
LastEditTime: 2021-11-25 23:18:16
Description: Space Navigation
FilePath: CF1481A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        x, y = map(int, input().strip().split())
        orders = input().strip()
        u, d, r, l = orders.count("U"), orders.count(
            "D"), orders.count("R"), orders.count("L")
        if -l <= x <= r and -d <= y <= u:
            print("YES")
        else:
            print("NO")


if __name__ == '__main__':
    func()
