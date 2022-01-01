#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-08 23:31:43
LastEditTime: 2021-11-08 23:36:51
Description: Quasi-palindrome
FilePath: CF863A.py
'''


def func():
    num = input().strip()
    while num.endswith("0"):
        num = num[:-1]

    print("YES" if num == num[::-1] else "NO")


if __name__ == '__main__':
    func()
