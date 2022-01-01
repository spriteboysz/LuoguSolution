#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-14 23:33:50
LastEditTime: 2021-12-14 23:44:50
Description: LJESTVICA 
FilePath: P7644.py
'''


def func():
    music = list(input().strip().split("|"))
    a, c = 0, 0
    for item in music:
        if item[0] in ["A", "D", "E"]:
            a += 1
        elif item[0] in ["C", "F", "G"]:
            c += 1
    if a > c:
        print("A-mol")
    elif a < c:
        print("C-dur")
    else:
        if music[-1][-1] in ["A", "D", "E"]:           
            print("A-mol")
        else:
            print("C-dur")


if __name__ == '__main__':
    func()
