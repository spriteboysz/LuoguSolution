#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 23:59:34
Description: 爱与愁的心痛
FilePath: P1614.py
'''

def func():
    n, m = map(int, input().strip().split())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
        
    minimum = sum(lst) + 1
    for i in range(0, n - m + 1):
        total = sum(lst[i:(i + m)])
        if total < minimum:
            minimum = total
    print(minimum)
        
        
if __name__ == '__main__':
    func()
    