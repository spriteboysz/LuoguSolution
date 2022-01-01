#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-18 23:47:36
LastEditTime: 2021-11-18 23:52:46
Description: Olesya and Rodion
FilePath: CF584A.py
'''


def func():
    n, t = map(int, input().strip().split())
    ans = (10 ** n - 1) - (10 ** n - 1) % t
    print(-1 if ans == 0 else ans)


if __name__ == '__main__':
    func()
