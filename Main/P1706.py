#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-02 16:40:02
LastEditTime: 2022-01-02 17:04:48
Description: 全排列问题
FilePath: P1706.py
'''


def func():
    n = int(input())
    number = [str(i) for i in range(1, n + 1)]
    for i in range(10 ** (n - 1), 10 ** n):
        if list(sorted(list(set(str(i))))) == number:
            print((" " * 5).join(str(i)))

if __name__ == '__main__':
    func()
    