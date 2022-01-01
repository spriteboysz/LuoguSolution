#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-14 00:03:02
LastEditTime: 2021-12-03 23:26:05
Description: Proper Nutrition
FilePath: CF898B.py
'''


def func():
    n = int(input())
    a, b = int(input()), int(input())
    for x in range(0, n // a + 1):
        if (n - x * a) % b == 0:
            print("YES")
            print(x, (n - a * x) // b)
            break
    else:
        print("NO")


if __name__ == '__main__':
    func()
