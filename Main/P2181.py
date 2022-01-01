#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-07 00:02:08
Description: 对角线
FilePath: P2181.py
'''

def func():
    n = int(input())
    print(n * (n - 1) * (n - 2) * (n - 3) // 24)

    
if __name__ == '__main__':
    func()
    