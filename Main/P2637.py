#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-21 23:06:02
LastEditTime: 2021-12-21 23:24:03
Description: 第一次，第二次，成交！
FilePath: P2637.py
'''


def func():
    n, m = map(int, input().strip().split())
    haystack = []
    for _ in range(m):
        price = input().strip()
        if price == "":
            price = input().strip()
        haystack.append(int(price))
    haystack = sorted(haystack, reverse=True)
    cost = []
    for i, v in enumerate(haystack):
        cost.append([v, v * (i + 1)])
    print(" ".join(map(str, max(cost, key=lambda el: el[1]))))


if __name__ == '__main__':
    func()
