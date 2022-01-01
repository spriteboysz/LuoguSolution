#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-09 23:02:43
Description: 阿克曼(Ackmann)函数 
FilePath: B2144.py
'''


def akm(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return akm(m - 1, 1)
    else:
        return akm(m - 1, akm(m, n - 1))
    

def func():
    m, n = map(int, input().strip().split())
    print(akm(m, n))


if __name__ == '__main__':
    func()
    