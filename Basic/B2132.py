#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-21 23:27:13
LastEditTime: 2021-10-21 23:36:58
Description: 素数对
FilePath: B2132.py
'''


def func():
    n = int(input())

    lst, num, flag = [2], 3, True
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

    flag = False
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] == 2:
            flag = True
            print(lst[i], lst[i + 1])
    if not flag:
        print("empty")


if __name__ == '__main__':
    func()
