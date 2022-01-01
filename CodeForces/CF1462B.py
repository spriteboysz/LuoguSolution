#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 22:54:17
LastEditTime: 2021-11-25 23:54:09
Description: Last Year's Substring
FilePath: CF1462B.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        if n < 4:
            print("NO")
        else:
            if s.startswith("2020") or s.endswith("2020"):
                print("YES")
            elif s.startswith("2") and s.endswith("020"):
                print("YES")
            elif s.startswith("20") and s.endswith("20"):
                print("YES")
            elif s.startswith("202") and s.endswith("0"):
                print("YES")
            else:
                print("NO")


if __name__ == '__main__':
    func()
