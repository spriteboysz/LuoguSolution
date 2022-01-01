#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-29 22:52:48
LastEditTime: 2021-11-29 22:57:43
Description: Valera and Antique Items
FilePath: CF441A.py
'''


def func():
    n, v = map(int, input().strip().split())
    deal = []
    for i in range(n):
        k, *s = map(int, input().strip().split())
        if v > min(s):
            deal.append(str(i + 1))
            
    print(len(deal))
    print(" ".join(deal))


if __name__ == '__main__':
    func()
