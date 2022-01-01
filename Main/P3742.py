#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-09 23:50:50
LastEditTime: 2021-12-09 23:53:13
Description: umi的函数
FilePath: P3742.py
'''


def func():
    n = int(input())
    s1 = input().strip()
    s2 = input().strip()
    for i in range(n):
        if s1[i] < s2[i]:
            print(-1)
            break
    else:
        print(s2)

if __name__ == '__main__':
    func()
    