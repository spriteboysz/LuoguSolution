#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-17 23:08:52
LastEditTime: 2021-11-17 23:16:15
Description: Infinity Gauntlet
FilePath: CF987A.py
'''


def func():
    gems = [["Power", "purple"], ["Time", "green"], ["Space", "blue"], [
        "Soul", "orange"], ["Reality", "red"], ["Mind", "yellow"]]

    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(input().strip())

    print(6 - n)
    for item in gems:
        if item[1] not in lst:
            print(item[0])


if __name__ == '__main__':
    func()
