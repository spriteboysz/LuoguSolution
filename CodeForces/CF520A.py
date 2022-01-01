#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-06 22:20:57
LastEditTime: 2021-11-20 23:55:22
Description: Pangram
FilePath: CF520A.py
'''


def func():
    _ = int(input())
    s = input().strip().lower()
    base = [False] * 26
    for item in s:
        base[ord(item) - ord("a")] = True
        if all(base):
            print("YES")
            break
    else:
        print("NO")


if __name__ == '__main__':
    func()
