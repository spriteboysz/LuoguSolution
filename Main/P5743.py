#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 21:58:08
LastEditTime: 2021-10-10 22:01:34
Description: 猴子吃桃
FilePath: P5743.py
'''


def count(n):
    if n == 1:
        return n
    else:
        return (count(n - 1) + 1) * 2


def func():
    n = int(input())
    print(count(n))


if __name__ == '__main__':
    func()
