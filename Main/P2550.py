#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-11 23:05:27
LastEditTime: 2021-10-11 23:18:56
Description: 彩票摇奖
FilePath: P2550.py
'''


def func():
    n = int(input())
    win = set(map(int, input().strip().split()))
    lst = [0] * 7
    for i in range(n):
        row = set(map(int, input().strip().split()))
        index = len(row & win)
        if index != 0:
            lst[0 - index] += 1

    print(" ".join(map(str, lst)))


if __name__ == '__main__':
    func()
