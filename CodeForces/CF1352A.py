#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-13 21:42:38
LastEditTime: 2021-11-13 21:52:45
Description: Sum of Round Numbers
FilePath: CF1352A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        num = input().strip()
        count, roundnumbers = 0, []
        for index, item in enumerate(num):
            if item != "0":
                count += 1
                roundnumbers.append(item + "0" * (len(num) - index - 1))
        print(count)
        print(" ".join(roundnumbers))


if __name__ == '__main__':
    func()
