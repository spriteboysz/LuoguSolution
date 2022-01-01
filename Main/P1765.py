#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-14 23:12:08
LastEditTime: 2021-10-14 23:20:43
Description: 手机
FilePath: P1765.py
'''


def func():
    s = input()
    lst = ["adgjmptw ", "behknqux", "cfilorvy", "sz"]
    count = 0
    for item in s:
        for i in range(len(lst)):
            if item in lst[i]:
                count += i + 1

    print(count)


if __name__ == '__main__':
    func()
