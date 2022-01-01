#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-25 00:03:37
LastEditTime: 2021-11-25 22:52:43
Description: File Name
FilePath: CF978B.py
'''


def func():
    n = int(input())
    name = input().strip()
    x = [1] * n
    for i in range(1, n):
        if name[i - 1] == "x" and name[i] == "x":
            x[i] = x[i - 1] + 1
            x[i - 1] = 0
        if name[i] != "x":
            x[i] = 0
            
    print(sum(map(lambda el: el - 2, filter(lambda el: el >= 3, x))))


if __name__ == '__main__':
    func()
