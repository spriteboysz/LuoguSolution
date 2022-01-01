#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-02 23:41:36
LastEditTime: 2021-12-03 22:14:12
Description: Bussiness trip
FilePath: CF149A.py
'''


def func():
    k = int(input())
    month = list(sorted((map(int, input().strip().split())), reverse=True))
    if k == 0:
        return 0
    else:
        for i in range(12):
            if sum(month[:(i + 1)]) >= k:
                return i + 1
        else:
            return -1

if __name__ == '__main__':
    ans = func()
    print(ans)
