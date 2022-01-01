#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 23:44:25
LastEditTime: 2021-10-10 23:49:52
Description: 宇宙总统
FilePath: P1781.py
'''


def func():
    n = int(input())
    no, mmax = 0, -1
    for i in range(1, n + 1):
        vote = int(input())
        if vote > mmax:
            no, mmax = i, vote

    print(no)
    print(mmax)


if __name__ == '__main__':
    func()
