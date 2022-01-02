#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-02 17:08:58
LastEditTime: 2022-01-02 17:21:10
Description: 小凯的数字
FilePath: P4942.py
'''


def func():
    q = int(input())
    for _ in range(q):
        l, r = map(int, input().strip().split())
        if (l + r) % 2 == 0:
            m, n = (l + r) // 2, r - l + 1
        else:
            m, n = l + r, (r - l + 1) // 2
        print(((m % 9) * (n % 9)) % 9)


if __name__ == '__main__':
    func()
