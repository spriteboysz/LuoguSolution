#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-21 00:14:34
LastEditTime: 2021-10-21 22:59:21
Description: 素数个数
FilePath: B2128.py
'''


def func():
    n = int(input())

    lst = [2]
    flag = True
    num = 3
    while num <= n:
        for i in lst:
            if num % i == 0:
                flag = False
                break
            if i > num ** 0.5 + 1:
                flag = True
                break
        if flag == True:
            lst.append(num)
        num += 2

    print(len(lst))


if __name__ == '__main__':
    func()
