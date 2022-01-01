#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-24 23:49:50
LastEditTime: 2021-11-24 23:53:42
Description: Book Reading
FilePath: CF884A.py
'''


def func():
    n, t = map(int, input().strip().split())
    time = list(map(int, input().strip().split()))
    total = 0
    for i in range(len(time)):
        total += 86400 - time[i]
        if total >= t:
            print(i + 1)
            break
    


if __name__ == '__main__':
    func()
    