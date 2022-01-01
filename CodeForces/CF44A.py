#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 23:20:47
LastEditTime: 2021-11-03 23:25:29
Description: Indian Summer
FilePath: CF44A.py
'''


def func():
    n = int(input())
    leaves = []
    for _ in range(n):
        tree, color = input().strip().split()
        if [tree, color] not in leaves:
            leaves.append([tree, color])
    return len(leaves)


if __name__ == '__main__':
    ans = func()
    print(ans)
