#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-03 23:04:35
LastEditTime: 2022-01-03 23:22:27
Description: 东风谷早苗
FilePath: P1724.py
'''


def func():
    direction = input().strip()
    t = int(input())
    div, mod = divmod(t, len(direction))
    x, y = (direction.count("E") - direction.count("W")) * \
        div, (direction.count("N") - direction.count("S")) * div
    direction = direction[:mod]
    x += direction.count("E") - direction.count("W")
    y += direction.count("N") - direction.count("S")
    print(x, y)


if __name__ == '__main__':
    func()
