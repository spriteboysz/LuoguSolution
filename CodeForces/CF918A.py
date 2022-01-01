#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-14 16:56:38
LastEditTime: 2021-11-14 17:06:44
Description: Eleven
FilePath: CF918A.py
'''


def func():
    n = int(input())
    lst = [0, 1, 1]
    for i in range(3, 20):
        lst.append(lst[i - 2] + lst[i - 1])
    #print(lst)
    for j in range(1, n + 1):
        if j in lst:
            print("O", end="")
        else:
            print("o", end="")
    print()


if __name__ == '__main__':
    func()
    