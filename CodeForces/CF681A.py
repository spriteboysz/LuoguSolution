#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 16:09:06
LastEditTime: 2021-11-07 16:14:17
Description: A Good Contest
FilePath: CF681A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        _, before, after = input().strip().split()
        if int(before) >= 2400 and int(after) > int(before):
            print("YES")
            break
    else:
        print("NO")


if __name__ == '__main__':
    func()
