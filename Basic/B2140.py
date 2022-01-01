#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-31 23:09:10
LastEditTime: 2021-10-31 23:13:23
Description: 二进制分类
FilePath: B2140.py
'''


def func():
    n = int(input())
    lst = []
    for i in range(1, n + 1):
        s2 = bin(i).replace("0b", "")
        if s2.count("1") > s2.count("0"):
            lst.append("A")
        else:
            lst.append("B")

    print(lst.count("A"), lst.count("B"))


if __name__ == '__main__':
    func()
