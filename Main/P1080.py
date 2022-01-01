#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-13 23:01:35
LastEditTime: 2021-12-13 23:14:50
Description: 国王游戏
FilePath: P1080.py
'''


def func():
    n = int(input())
    king = tuple(map(int, input().strip().split()))
    minister = []
    for _ in range(n):
        minister.append(tuple(map(int, input().strip().split())))
    minister = sorted(minister, key=lambda el: el[0] * el[1])
    gold = []
    left, right = king[0], king[1]
    for item in minister:
        gold.append(left // item[1])
        left *= item[0]
    print(max(gold))


if __name__ == '__main__':
    func()
