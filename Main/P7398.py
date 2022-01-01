#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-27 22:45:46
LastEditTime: 2021-10-27 22:54:38
Description: Sifra
FilePath: P7398.py
'''


def func():
    s1 = input().strip()
    s2 = ""
    for i in range(len(s1)):
        if not s1[i].isdigit():
            s2 += " "
        else:
            s2 += s1[i]
    print(len(set(s2.split())))


if __name__ == '__main__':
    func()
