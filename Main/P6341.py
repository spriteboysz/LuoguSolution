#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-30 23:48:51
LastEditTime: 2021-12-31 00:12:11
Description: PRAVOKUTNI
FilePath: P6341.py
'''


def distance2(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def func():
    n = int(input())
    point = []
    for _ in range(n):
        point.append(list(map(int, input().strip().split())))

    distance = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            distance.append(
                distance2(point[i][0], point[i][1], point[j][0], point[j][1]))
    distance = sorted(distance)
    print(distance)
    count = 0
    for a in range(len(distance) - 2):
        for b in range(a + 1, len(distance) - 1):
            for c in range(b + 1, len(distance)):
                if distance[a] + distance[b] == distance[c]:
                    print(distance[a], distance[b], distance[c])
                    count += 1
    print(count)


if __name__ == '__main__':
    func()
