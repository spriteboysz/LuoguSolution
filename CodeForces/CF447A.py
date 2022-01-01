#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-29 22:58:49
LastEditTime: 2021-11-29 23:08:17
Description: DZY Loves Hash
FilePath: CF447A.py
'''


def func():
    p, n = map(int, input().strip().split())
    lst = []
    flag = False
    for i in range(n):
        num = int(input()) % p
        if num not in lst:
            lst.append(num)
        elif not flag:
            print(i + 1)
            flag = True
    if not flag:
        print(-1)


if __name__ == '__main__':
    func()
