#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-11 23:44:23
LastEditTime: 2021-12-12 22:19:23
Description: 东南西北
FilePath: P2689.py
'''


def func():
    x1, y1 = map(int, input().strip().split())
    x2, y2 = map(int, input().strip().split())
    t = int(input())
    direction = []
    for _ in range(t):
        direction.append(input().strip())
    x, y = x2 - x1, y2 - y1
    path = []
    path.extend(["E"] * x) if x > 0 else path.extend(["W"] * abs(x))
    path.extend(["N"] * y) if y > 0 else path.extend(["S"] * abs(y))
    #!题目要求最小的步数，而非最小的时间
    count = 0
    for el in direction:
        if el in path:
            count += 1
            path.remove(el)
        if len(path) == 0:
            print(count)
            break
    else:
        print(-1)


if __name__ == '__main__':
    func()
