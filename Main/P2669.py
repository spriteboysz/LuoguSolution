#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-07 23:47:10
Description: 金币
FilePath: P2669.py
'''

def func():
    k = int(input())

    count, base, times = 0, 1, 1
    for i in range(1, k + 1):    
        for j in range(1, base + 1):
            count += base
            if times == k:
                print(count)
                return
            times += 1
        base += 1

if __name__ == '__main__':
    func()
    