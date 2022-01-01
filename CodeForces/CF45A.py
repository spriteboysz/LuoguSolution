#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-03 23:13:53
LastEditTime: 2021-11-03 23:15:00
Description: Codecraft III
FilePath: CF45A.py
'''


def func():
    months = ["January", "February", "March", "April", "May", "June",
              "July", "August", "September", "October", "November", "December"]
    s, k = input().strip(), int(input())
    return months[(months.index(s) + k) % 12]


if __name__ == '__main__':
    ans = func()
    print(ans)
