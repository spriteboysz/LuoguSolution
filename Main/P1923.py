#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-11 22:48:32
LastEditTime: 2021-12-12 23:13:04
Description: 求第k小的数
FilePath: P1923.py
'''

def func():
    n, k = map(int, input().strip().split())
    lst = list(sorted(map(int, input().strip().split())))
    print(lst[k])


if __name__ == '__main__':
    func()
    
