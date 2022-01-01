#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 13:40:02
LastEditTime: 2021-11-26 13:44:03
Description: Spy Detected!
FilePath: CF1512A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        lst = list(map(int, input().strip().split()))
        index = list(map(lambda el: lst.count(el), lst)).index(1)
        print(index + 1)


if __name__ == '__main__':
    func()
