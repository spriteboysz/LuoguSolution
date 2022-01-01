#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-21 23:28:40
LastEditTime: 2021-12-21 23:33:29
Description: 硬币翻转
FilePath: P2708.py
'''


def func():
    coin = list(input().strip())
    count = 0
    for i in range(len(coin) - 1):
        if coin[i] != coin[i + 1]:
            count += 1
    if coin[-1] == "0":
        count += 1
    print(count)


if __name__ == '__main__':
    func()
