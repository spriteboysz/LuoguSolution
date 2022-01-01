#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 23:51:04
Description: 冰雹猜想
FilePath: P5727.py
'''

def func():
    n = int(input())
    lst = []
    while n > 1:
        if n % 2 == 0:
            lst.append(str(n))
            n = n // 2
        else:
            lst.append(str(n))
            n = n * 3 + 1
    lst.append("1")
    print(" ".join(reversed(lst)))

if __name__ == '__main__':
    func()
    
