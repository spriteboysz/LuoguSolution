#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 13:23:41
LastEditTime: 2021-11-26 13:28:19
Description: Balanced Substring
FilePath: CF1569A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        s = input().strip()
        for i in range(n - 1):
            if s[i] == "a" and s[i + 1] == "b":
                print(i + 1, i + 2)
                break
            elif s[i] == "b" and s[i + 1] == "a":
                print(i + 1, i + 2)
                break
        else:
            print(-1, -1)


if __name__ == '__main__':
    func()
