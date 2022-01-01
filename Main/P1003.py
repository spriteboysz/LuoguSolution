#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-04 22:50:59
LastEditTime: 2021-12-04 22:59:35
Description: [NOIP2011 提高组] 铺地毯
FilePath: P1003.py
'''


def func():
    n = int(input())
    carpets = []
    for _ in range(n):
        a, b, g, k = map(int, input().strip().split())
        carpets.append([a, a + g, b, b + k])
    x, y = map(int, input().strip().split())

    for i in range(n - 1, -1, -1):
        if carpets[i][0] <= x <= carpets[i][1] and carpets[i][2] <= y <= carpets[i][3]:
            print(i + 1)
            break
    else:
        print(-1)


if __name__ == '__main__':
    func()
