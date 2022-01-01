#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 23:07:28
Description: 质因数分解
FilePath: B2084.py
'''

def func():
    n = int(input())
    if n % 2 == 0:
        print(n // 2)
        return 
    
    for i in range(3, n, 2):
        if n % i == 0:
            print(n // i)
            return


if __name__ == '__main__':
    func()
    
