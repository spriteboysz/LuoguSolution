#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-25 23:02:50
LastEditTime: 2021-11-25 23:12:01
Description: Replacing Elements
FilePath: CF1473A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n, d = map(int, input().strip().split())
        lst = list(map(int, input().strip().split()))
        if max(lst) <= d:
            print("YES")
        else:
            minium1 = min(lst)
            lst.remove(minium1)
            minium2 = min(lst)
            if minium1 + minium2 <= d:
                print("YES")
            else:
                print("NO")


if __name__ == '__main__':
    func()
