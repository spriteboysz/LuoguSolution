#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-01 15:27:59
LastEditTime: 2022-01-01 15:40:06
Description: 玩具谜题
FilePath: P1563.py
'''


def func():
    n, m = map(int, input().strip().split())
    puppet = []
    for _ in range(n):
        orientation, occupation = input().strip().split()
        puppet.append([int(orientation), occupation])

    current = 0
    for _ in range(m):
        a, s = map(int, input().strip().split())
        if a == 0:
            if puppet[current][0] == 0:
                current = (current + n - s) % n
            else:
                current = (current + s) % n
        else:
            if puppet[current][0] == 0:
                current = (current + s) % n
            else:
                current = (current + n - s) % n
    print(puppet[current][1])


if __name__ == '__main__':
    func()
