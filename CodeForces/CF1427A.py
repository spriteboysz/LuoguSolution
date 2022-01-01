#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-18 00:01:02
LastEditTime: 2021-11-18 22:58:43
Description: Avoiding Zero
FilePath: CF1427A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        _ = int(input())
        lst = list(map(int, input().strip().split()))
        if sum(lst) == 0:
            print("NO")
        else:
            print("YES")
            if sum(lst) > 0:
                lst = sorted(lst, reverse=True)
            elif sum(lst) < 0:
                lst = sorted(lst)
            print(" ".join(map(str, lst)))


if __name__ == '__main__':
    func()
