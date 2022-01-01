#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-23 23:13:27
LastEditTime: 2021-10-23 23:18:29
Description: BIJELE
FilePath: P6336.py
'''


def func():
    cur = list(map(int, input().strip().split()))
    chess = [1, 1, 2, 2, 2, 8]

    action = []
    for i in range(6):
        action.append(str(chess[i] - cur[i]))
    print(" ".join(action))


if __name__ == '__main__':
    func()
    