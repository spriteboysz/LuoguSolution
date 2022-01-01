#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-13 23:40:11
LastEditTime: 2021-11-13 23:48:07
Description: Fake News (easy) 
FilePath: CF802G.py
'''


def func():
    s = input().strip()
    key = "heidi"
    i = 0
    for item in s:
        if item == key[i]:
            i += 1
        if i == 5:
            print("YES")
            break
    else:
        print("NO")


if __name__ == '__main__':
    func()
