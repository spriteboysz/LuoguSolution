#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-24 17:53:35
LastEditTime: 2021-10-24 20:05:59
Description: Trol
FilePath: P7199.py
'''


def func():
    n = int(input())
    for _ in range(n):
        a, b = map(int, input().strip().split())
        total = 0
        for i in range(a, b + 1):
            if i % 9 == 0:
                total += 9
            else:
                total += i % 9
            
        print(total)


if __name__ == '__main__':
    func()
