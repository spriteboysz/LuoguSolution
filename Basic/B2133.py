#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-10 22:04:27
LastEditTime: 2021-12-10 22:10:36
Description:我家的门牌号 
FilePath: B2133.py
'''


def func():
    n = int(input())
    total = 0
    for i in range(1, 10001):
        total += i
        for j in range(1, i + 1):
            if total - j * 3 == n:
                print(j, i)
                return


if __name__ == '__main__':
    func()
