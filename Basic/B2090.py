#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 16:54:05
Description: 年龄与疾病
FilePath: B2090.py
'''


def func():
    n = int(input())
    ages = list(map(int, input().strip().split()))
    count = [0, 0, 0, 0]
    for i in range(n):
        if 0 <= ages[i] <= 18:
            count[0] += 1
        elif 19 <= ages[i] <= 35:
            count[1] += 1
        elif 36 <= ages[i] <= 60:
            count[2] += 1
        else:
            count[3] += 1

    for i in range(4):
        print("%.2f%%" % (count[i] / n * 100))


if __name__ == '__main__':
    func()
