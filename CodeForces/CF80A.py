#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-03 21:57:09
LastEditTime: 2021-12-03 21:59:49
Description: 
FilePath: CF80A.py
'''


def func():
    prime = [0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    n, m = map(int, input().strip().split())
    if m in prime and prime.index(m) - prime.index(n) == 1:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
