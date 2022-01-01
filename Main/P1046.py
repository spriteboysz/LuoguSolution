#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-06 15:14:03
Description: 陶陶摘苹果
FilePath: P1046.py
'''

def func():
    lst = list(map(int, input().strip().split()))
    high = int(input())

    count = 0
    for item in lst:
        if item <= high + 30:
            count += 1

    print(count)

if __name__ == '__main__':
    func()
    
