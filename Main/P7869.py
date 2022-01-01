#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-15 23:55:58
LastEditTime: 2021-12-16 00:01:43
Description: 
FilePath: P7869.py
'''


def func():
    s = input().strip()
    if r"\r\n" in s:
        print("windows")
    elif r"\n" in s:
        print("linux")
    elif r"\r" in s:
        print("mac")


if __name__ == '__main__':
    func()
