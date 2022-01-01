#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-26 17:32:36
LastEditTime: 2021-12-26 17:41:04
Description: 
FilePath: P6402.py
'''


def func():
    n = int(input())
    contestant = {}
    for _ in range(n):
        name = input().strip()
        if name in contestant.keys():
            contestant[name] += 1
        else:
            contestant[name] = 1
    
    for _ in range(n - 1):
        name = input().strip()
        contestant[name] -= 1

    for k, v in contestant.items():
        if v > 0:
            print(k)
            break
    else:
        print(-1)


if __name__ == '__main__':
    func()
    