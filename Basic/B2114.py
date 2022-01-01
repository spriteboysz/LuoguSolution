#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-20 22:20:03
LastEditTime: 2021-10-20 22:31:37
Description: 配对碱基链
FilePath: B2114.py
'''


def func():
    s1 = input().strip()

    s2 = ""
    mapping = ["A", "T", "C", "G", "T", "A", "G", "C"]
    for item in s1:
        s2 += mapping[mapping.index(item) + 4]
    print(s2)


if __name__ == '__main__':
    func()
