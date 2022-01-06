#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-06 23:05:42
LastEditTime: 2022-01-06 23:33:09
Description: 眼红的Medusa
FilePath: P1571.py
'''


def func():
    n, m = map(int, input().strip().split())
    if n != 0 or m != 0:
        innovate = input().strip().split()
        special = input().strip().split()
        dic = dict(zip(special, special))
        double = []
        for v in innovate:
            if v in dic:
                double.append(v)
        print(" ".join(double))


if __name__ == '__main__':
    func()
