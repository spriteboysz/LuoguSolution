#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-19 22:10:40
LastEditTime: 2021-12-19 22:38:08
Description: 赵神牛的游戏
FilePath: P2006.py
'''


def func():
    k, m, n = map(int, input().strip().split())
    lst = []
    for i in range(m):
        a, b = map(float, input().strip().split())
        if a == 0 and b != 0:
            lst.append(str(i + 1))
        elif k // a * b >= n:
            lst.append(str(i + 1))
    print(" ".join(lst) if len(lst) != 0 else -1)


if __name__ == '__main__':
    func()
