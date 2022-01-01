#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-09 23:08:22
LastEditTime: 2021-11-09 23:17:53
Description: Suffix Three
FilePath: CF1281A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        s = input().strip()
        if s.endswith("po"):
            print("FILIPINO")
        if s.endswith("desu") or s.endswith("masu"):
            print("JAPANESE")
        if s.endswith("mnida"):
            print("KOREAN")


if __name__ == '__main__':
    func()
