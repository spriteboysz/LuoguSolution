#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-14 16:32:16
LastEditTime: 2021-11-27 23:39:01
Description: Chat room
FilePath: CF58A.py
'''


def func():
    s = input().strip()
    key = "hello"
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
    