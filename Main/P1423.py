#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 22:17:06
Description: 小玉在游泳
FilePath: P1423.py
'''

def func():
    s = float(input())

    step, cur, count = 2, 0, 0
    while cur <= s:
        cur += step
        step *= 0.98
        count += 1 
    print(count)

if __name__ == '__main__':
    func()
    