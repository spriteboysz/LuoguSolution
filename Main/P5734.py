#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-06 23:55:26
LastEditTime: 2021-12-07 00:13:17
Description: 文字处理软件
FilePath: P5734.py
'''


def func():
    q = int(input())
    s = input().strip()
    for _ in range(q):
        operator, *args = input().strip().split()
        if operator == "1":
            s += args[0]
            print(s)
        elif operator == "2":
            s = s[int(args[0]):(int(args[0]) + int(args[1]))]
            print(s)
        elif operator == "3":
            s = s[0:int(args[0])] + args[1] + s[int(args[0]):]
            print(s)
        elif operator == "4":
            print(s.find(args[0]))


if __name__ == '__main__':
    func()
