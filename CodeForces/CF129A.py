#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-27 23:30:46
LastEditTime: 2021-11-27 23:36:11
Description: Cookies
FilePath: CF129A.py
'''


def func():
    _ = int(input())
    cookies = list(map(int, input().strip().split()))
    if sum(cookies) % 2 == 0:
        print(len(list(filter(lambda el: el % 2 == 0, cookies))))
    else:
        print(len(list(filter(lambda el: el % 2 != 0, cookies))))


if __name__ == '__main__':
    func()
