#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-09 23:06:36
LastEditTime: 2021-12-09 23:25:58
Description: honoka的键盘
FilePath: P3741.py
'''


def func():
    n = int(input())
    s = list(input().strip())
    count = 0
    for i in range(n - 1):
        if s[i] == "V" and s[i + 1] == "K":
            count += 1
            s[i], s[i + 1] = "v", "k"
    for i in range(n - 1):
        if s[i] == "V" and s[i + 1] == "V":
            count += 1
            break
        if s[i] == "K" and s[i + 1] == "K":
            count += 1
            break
    print(count)


if __name__ == '__main__':
    func()
