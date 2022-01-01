#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-23 21:10:08
LastEditTime: 2021-10-23 21:14:00
Description: 培训
FilePath: P5744.py
'''


def func():
    n = int(input())
    for _ in range(n):
        name, age, point = input().strip().split()
        age = int(age) + 1
        point = min(int(int(point) * 1.2), 600)
        print(name, age, point)


if __name__ == '__main__':
    func()
