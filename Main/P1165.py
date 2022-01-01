#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-17 22:20:31
LastEditTime: 2021-12-18 13:55:27
Description: 日志分析
FilePath: P1165.py
'''


def func():
    n = int(input())
    storehouse = []
    for _ in range(n):
        s = input()
        if s[0] is "0":
            storehouse.append(int(s.split()[1]))
        elif s[0] is "1" and len(storehouse) >= 1:
            storehouse.pop(-1)
        elif s[0] is "2":
            print(max(storehouse) if len(storehouse) != 0 else 0)


if __name__ == '__main__':
    func()
