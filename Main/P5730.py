#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-05 22:33:52
LastEditTime: 2021-12-05 23:04:49
Description: 显示屏
FilePath: P5730.py
'''


def func():
    base = ["XXX...X.XXX.XXX.X.X.XXX.XXX.XXX.XXX.XXX.",
            "X.X...X...X...X.X.X.X...X.....X.X.X.X.X.",
            "X.X...X.XXX.XXX.XXX.XXX.XXX...X.XXX.XXX.",
            "X.X...X.X.....X...X...X.X.X...X.X.X...X.",
            "XXX...X.XXX.XXX...X.XXX.XXX...X.XXX.XXX."]
    n = int(input())
    num = input().strip()
    row = [""] * 5
    for item in num:
        for j in range(5):
            row[j] += base[j][(4*int(item)):(4*int(item)+4)]
    for j in range(5):
        print(row[j][:-1])


if __name__ == '__main__':
    func()
