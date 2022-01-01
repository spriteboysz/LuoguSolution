#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-13 23:51:04
LastEditTime: 2021-11-13 23:59:55
Description: Scarborough Fair
FilePath: CF897A.py
'''


def func():
    _, m = map(int, input().strip().split())
    s = list(input().strip())
    for _ in range(m):
        l, r, c1, c2 = input().strip().split() 
        for i in range(int(l) - 1, int(r)):
            if s[i] == c1:
                s[i] = c2
    print("".join(s))


if __name__ == '__main__':
    func()
    