#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-18 23:11:14
LastEditTime: 2021-11-18 23:17:28
Description: Wet Shark and Odd and Even
FilePath: CF621A.py
'''


def func():
    _ = int(input())
    lst = list(map(int, input().strip().split()))
    if sum(lst) % 2 == 0:
        print(sum(lst))
    else:
        odd = filter(lambda el: el % 2 != 0, lst)
        print(sum(lst) - min(odd))


if __name__ == '__main__':
    func()
