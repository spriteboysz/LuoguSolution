#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-29 22:39:32
LastEditTime: 2021-12-29 22:44:30
Description: 谁能赢呢？
FilePath: P4136.py
'''


def func():
    while True:
        n = int(input())
        if n == 0:
            break
        else:
            print("Alice" if n % 2 == 0 else "Bob")


if __name__ == '__main__':
    func()
