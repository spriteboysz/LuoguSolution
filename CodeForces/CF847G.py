#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-08 23:49:56
LastEditTime: 2021-11-08 23:53:46
Description: University Classes
FilePath: CF847G.py
'''


def func():
    n = int(input())
    classroom = [0] * 7
    for _ in range(n):
        classes = list(input().strip())
        for i in range(7):
            classroom[i] += int(classes[i])
            
    print(max(classroom))


if __name__ == '__main__':
    func()
    