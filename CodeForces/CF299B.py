#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-01 23:50:55
LastEditTime: 2021-12-02 00:04:11
Description: Ksusha the Squirrel
FilePath: CF299B.py
'''


def func():
    n, k = map(int, input().strip().split())
    road = input().strip()
    if "#" in road:
        rock = list(filter(lambda el: el != "", road.split(".")))
        num = max(map(lambda el: len(el), rock))
        print("YES" if num < k else "NO")
    else:
        print("YES")


if __name__ == '__main__':
    func()
