#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-02 23:49:11
LastEditTime: 2021-11-28 22:21:11
Description: Cifera
FilePath: CF114A.py
'''


def func():
    k, l = int(input()), int(input())
    for n in range(1, l):
        if k ** n == l:
            print("YES")
            print(n - 1)
            return
        elif k ** n > l:
            break
    print("NO")


if __name__ == '__main__':
    func()
