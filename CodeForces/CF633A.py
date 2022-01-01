#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-06 23:08:27
LastEditTime: 2021-11-06 23:27:23
Description: Ebony and Ivory
FilePath: CF633A.py
'''

def func():
    a, b, c = map(int, input().strip().split())
    for x in range(0, c + 1):
        y = c - a * x
        if y >= 0 and y % b == 0:
            print("YES")
            break
    else:
        print("NO")


if __name__ == '__main__':
    func()
    