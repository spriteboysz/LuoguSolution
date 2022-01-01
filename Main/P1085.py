#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-06 23:35:05
Description: 不高兴的津津
FilePath: P1085.py
'''

def func():
    t1, t2 = [0] * 7, [0] * 7
    for i in range(0, 7):
        t1[i], t2[i] = map(int, input().strip().split())

    for i in range(0, 7):
        if t1[i] + t2[i] > 8:
            print(i + 1)
            break
    else:
        print(0)

if __name__ == '__main__':
    func()
    