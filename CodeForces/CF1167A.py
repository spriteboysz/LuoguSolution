#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-19 22:26:15
LastEditTime: 2021-11-19 22:29:58
Description: Telephone Number
FilePath: CF1167A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        num = input().strip()
        for i in range(n):
            if num[i] == "8" and n - i >= 11:
                print("YES")
                break
        else:
            print("NO")


if __name__ == '__main__':
    func()
    