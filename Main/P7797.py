#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-18 15:06:16
LastEditTime: 2021-12-18 15:14:02
Description: BELA
FilePath: P7797.py
'''


def func():
    base = ["A", "K", "Q", "J", "T", "9", "8", "7"]
    special = [11, 4, 3, 20, 10, 14, 0, 0]
    normal = [11, 4, 3, 2, 10, 0, 0, 0]
    n, b = input().strip().split()
    count = 0
    for _ in range(4 * int(n)):
        card = input().strip()
        if card[1] == b:
            count += special[base.index(card[0])]
        else:
            count += normal[base.index(card[0])]
    print(count)


if __name__ == '__main__':
    func()
