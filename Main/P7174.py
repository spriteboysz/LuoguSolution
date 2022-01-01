#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-16 23:16:52
LastEditTime: 2021-12-16 23:21:04
Description: CESTA
FilePath: P7174.py
'''


def func():
    num = list(input().strip())
    if "0" in num and sum(map(int, num)) % 3 == 0:
        print("".join(sorted(num, reverse=True)))
    else:
        print(-1)


if __name__ == '__main__':
    func()
