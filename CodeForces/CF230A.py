#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-02 22:59:08
LastEditTime: 2021-11-02 23:05:55
Description: Dragons
FilePath: CF230A.py
'''


def func():
    s, n = map(int, input().strip().split())
    lst = []
    for _ in range(n):
        lst.append(list(map(int, input().strip().split())))
    lst = sorted(lst, key=lambda el: el[0])

    for item in lst:
        if s > item[0]:
            s += item[1]
        else:
            print("NO")
            break
    else:
        print("YES")


if __name__ == '__main__':
    func()
