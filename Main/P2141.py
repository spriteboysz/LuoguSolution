#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-10-15 22:39:25
LastEditTime: 2021-10-15 22:45:52
Description: 珠心算测验
FilePath: P2141.py
"""


def func():
    n = int(input())
    lst = list(map(int, input().strip().split()))

    total = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            total.append(lst[i] + lst[j])

    print(len(set(total) & set(lst)))


if __name__ == "__main__":
    func()
