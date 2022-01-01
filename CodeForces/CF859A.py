#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-08 23:37:46
LastEditTime: 2021-11-11 23:15:04
Description: Declined Finalists
FilePath: CF859A.py
'''


def func():
    _ = int(input())
    rank = max(map(int, input().strip().split()))
    print(0 if rank <= 25 else (rank - 25))


if __name__ == '__main__':
    func()
