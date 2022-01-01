#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-11 23:43:40
LastEditTime: 2021-11-11 23:46:02
Description: Vasya and Chocolate
FilePath: CF1065A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        s, a, b, c = map(int, input().strip().split())
        print(s // c + s // c // a * b)


if __name__ == '__main__':
    func()
    