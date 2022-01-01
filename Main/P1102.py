#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-29 21:51:43
LastEditTime: 2021-10-29 22:14:53
Description: 数对
FilePath: P1102.py
'''


def func():
    n, c = map(int, input().strip().split())
    lst = list(sorted(map(int, input().strip().split()), reverse=True))
    count = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lst[i] - lst[j] == c:
                count += 1
            elif lst[i] - lst[j] > c:
                break
    print(count)


if __name__ == '__main__':
    func()
    