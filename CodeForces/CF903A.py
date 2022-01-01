#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-14 17:09:34
LastEditTime: 2021-11-14 17:20:42
Description: Hungry Student Problem
FilePath: CF903A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        x = int(input())
        for i in range(0, x // 3 + 1):
            if x - i * 3 >= 0 and (x - i * 3) % 7 == 0:
                print("YES")
                break
        else:
            print("NO")


if __name__ == '__main__':
    func()
