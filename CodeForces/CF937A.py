#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-08 23:04:41
LastEditTime: 2021-11-08 23:07:02
Description: Olympiad
FilePath: CF937A.py
'''


def func():
    _ = int(input())
    points = map(int, input().strip().split())
    print(len(set(points) - set([0])))


if __name__ == '__main__':
    func()
