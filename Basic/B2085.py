#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-17 14:52:42
Description: 第n小的质数
FilePath: B2085.py
'''

def func():
    n = int(input())

    lst = [2]
    num = 3
    flag = True
    while len(lst) < n:
        for i in lst:
            if num % i == 0:
                flag = False
                break
            if i > num ** 0.5 + 1:
                flag = True
                break
        if flag:
            lst.append(num)
        num += 2
    print(lst[-1])


if __name__ == '__main__':
    func()
