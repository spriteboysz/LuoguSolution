#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-01 21:55:26
LastEditTime: 2021-12-01 22:02:15
Description: Ostap and Grasshopper
FilePath: CF735A.py
'''


def func():
    n, k = map(int, input().strip().split())
    s = input().strip()
    start = min(s.index("G"), s.index("T"))
    end = max(s.index("G"), s.index("T"))
    if (end - start) % k != 0:
        print("NO")
    else:
        for i in range(start, end + 1, k):
            if s[i] == "#":
                print("NO")
                break
        else:
            print("YES")


if __name__ == '__main__':
    func()
