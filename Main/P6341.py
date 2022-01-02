#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-30 23:48:51
LastEditTime: 2022-01-02 22:34:13
Description: PRAVOKUTNI
FilePath: P6341.py
'''


def func():
    n = int(input())
    point = []
    for _ in range(n):
        point.append(list(map(int, input().strip().split())))

    dic = {}

    def distance2(x1, y1, x2, y2):
        key = str([x1, y1, x2, y2])
        if key not in dic.keys():
            dic[key] = (x1 - x2) ** 2 + (y1 - y2) ** 2
        return dic[key]

    count = 0
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                a2 = distance2(point[i][0], point[i][1],
                               point[j][0], point[j][1])
                b2 = distance2(point[i][0], point[i][1],
                               point[k][0], point[k][1])
                c2 = distance2(point[k][0], point[k][1],
                               point[j][0], point[j][1])
                if a2 + b2 == c2 or a2 + c2 == b2 or b2 + c2 == a2:
                    count += 1
    print(count)


if __name__ == '__main__':
    func()
