#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-09 00:02:03
LastEditTime: 2021-11-09 00:06:09
Description: Text Volume
FilePath: CF837A.py
'''


def func():
    _ = int(input())
    words = input().strip().split()
    most = 0
    for word in words:
        count = 0
        for char in word:
            if char.isupper():
                count += 1
        if count > most:
            most = count
    print(most)


if __name__ == '__main__':
    func()
