#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 13:19:09
LastEditTime: 2021-10-24 13:23:39
Description: KEMIJA
FilePath: P6409.py
'''


def func():
    s = input().strip()
    vowel = ["a", "e", "i", "o", "u"]
    for item in vowel:
        s = s.replace(item+"p"+item, item)
    print(s)


if __name__ == '__main__':
    func()
