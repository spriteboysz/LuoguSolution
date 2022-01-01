#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-19 21:51:14
LastEditTime: 2021-12-19 22:00:37
Description: HXY玩卡片
FilePath: P2192.py
'''


def func():
    n = int(input())
    card = input().strip().split()
    card0, card5 = card.count("0"), card.count("5")
    if card0 == 0:
        print(-1)
    elif card5 < 9:
        print(0)
    else:
        print("5" * (card5 // 9 * 9) + "0" * card0)


if __name__ == '__main__':
    func()
