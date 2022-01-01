#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 22:44:22
LastEditTime: 2021-10-24 22:51:13
Description: 西游记公司
FilePath: P1615.py
'''


def func():
    start = list(map(int, input().strip().split(":")))
    end = list(map(int, input().strip().split(":")))
    speed = int(input())
    second = (end[0] - start[0]) * 3600 + \
        (end[1] - start[1]) * 60 + (end[2] - start[2])
    print(second * speed)


if __name__ == '__main__':
    func()
