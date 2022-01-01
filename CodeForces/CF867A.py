#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-30 23:02:00
LastEditTime: 2021-11-30 23:08:39
Description: Between the Offices
FilePath: CF867A.py
'''


def func():
    n = int(input())
    s = input().strip()
    count1, count2 = 0, 0
    for i in range(n - 1):
        if s[i] == "S" and s[i + 1] == "F":
            count1 += 1
        if s[i] == "F" and s[i + 1] == "S":
            count2 += 1
    print("YES" if count1 > count2 else "NO")


if __name__ == '__main__':
    func()
