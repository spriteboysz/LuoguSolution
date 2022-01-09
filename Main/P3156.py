#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 21:46:57
LastEditTime: 2022-01-09 22:11:00
Description: 询问学号
FilePath: P3156.py
'''


def func():
    n, m = [int(i) for i in input().strip().split()]
    num = list(map(int, input().strip().split()))
    ask = list(map(int, input().strip().split()))
    for item in ask:
        print(num[item - 1])


if __name__ == '__main__':
    func()
    