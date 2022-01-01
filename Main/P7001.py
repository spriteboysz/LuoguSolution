#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-05 17:07:55
LastEditTime: 2021-12-05 17:15:33
Description: Fraud Busters
FilePath: P7001.py
'''


def func():
    base = input().strip()
    n = int(input())
    lst = []
    for _ in range(n):
        s = input().strip()
        if len(s) != 9:
            continue
        for el1, el2 in zip(base, s):
            if el1 != "*" and el1 != el2:
                break
        else:
            lst.append(s)
    print(len(lst))
    print("\n".join(lst))


if __name__ == '__main__':
    func()
