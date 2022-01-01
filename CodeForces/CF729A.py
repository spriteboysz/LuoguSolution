#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 17:51:13
LastEditTime: 2021-11-07 22:30:12
Description: Interview with Oleg
FilePath: CF729A.py
'''


def func():
    _ = int(input())
    s = input().strip()
    while "ogogo" in s:
        s = s.replace("ogogo", "ogo")
    print(s.replace("ogo", "***"))


if __name__ == '__main__':
    func()
