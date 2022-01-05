#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-05 23:13:11
LastEditTime: 2022-01-05 23:51:53
Description: [USACO09OCT]Papaya Jungle G
FilePath: P2958.py
'''


def func():
    n, m = map(int, input().strip().split())
    papaya = [[0] * (m + 2) for _ in range(n + 2)]
    for i in range(n):
        papaya[i + 1][1:m + 1] = map(int, input().strip().split())

    count = 0
    i, j = 1, 1
    while True:
        count += papaya[i][j]
        papaya[i][j] = 0
        maximum = max(papaya[i - 1][j], papaya[i + 1][j],
                      papaya[i][j - 1], papaya[i][j + 1])
        if maximum == papaya[i - 1][j]:
            i = i - 1
        elif maximum == papaya[i + 1][j]:
            i = i + 1
        elif maximum == papaya[i][j - 1]:
            j = j - 1
        elif maximum == papaya[i][j + 1]:
            j = j + 1
        if i == n and j == m:
            count += papaya[i][j]
            break
    print(count)


if __name__ == '__main__':
    func()
