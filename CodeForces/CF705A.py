#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 16:43:41
LastEditTime: 2021-11-07 16:58:24
Description: Hulk
FilePath: CF705A.py
'''


def func():
    n = int(input())
    if n == 1:
        print("I hate it")
    else:
        feelings = "I hate that I love that " * (n // 2)
        if n % 2 == 0:
            feelings = feelings.strip()[:-4] + "it"
        else:
            feelings += "I hate it"
        print(feelings)


if __name__ == '__main__':
    func()
