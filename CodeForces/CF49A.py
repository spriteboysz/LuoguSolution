#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-02 00:05:26
LastEditTime: 2021-11-02 00:12:47
Description: Sleuth
FilePath: CF49A.py
'''


def func():
    s = input().strip().replace(" ", "")
    i = 1
    while not s[-i].isalpha():
        i += 1
        
    if s[-i].upper() in ["A", "E", "I", "O", "U", "Y"]:
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    func()
    