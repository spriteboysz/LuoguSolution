#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-30 22:45:15
LastEditTime: 2021-11-30 22:48:26
Description: Boy or Girl
FilePath: CF236A.py
'''


def func():
    name = input().strip()
    if len(set(list(name))) % 2 != 0:
        print("IGNORE HIM!")
    else:
        print("CHAT WITH HER!")


if __name__ == '__main__':
    func()
