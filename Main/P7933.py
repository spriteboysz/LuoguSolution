#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-16 00:14:21
LastEditTime: 2021-12-16 23:15:02
Description: 
FilePath: P7933.py
'''


def func():
    n = int(input())
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break
    else:
        i = n
        
    print(n - n // i)


if __name__ == '__main__':
    func()
