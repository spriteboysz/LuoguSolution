#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 23:31:58
LastEditTime: 2021-11-03 23:42:46
Description: Football
FilePath: CF43A.py
'''


def func():
    n = int(input())
    goals = []
    for _ in range(n):
        goals.append(input().strip())
    return sorted(list(set(goals)), key=lambda el: goals.count(el))[-1]


if __name__ == '__main__':
    ans = func()
    print(ans)
