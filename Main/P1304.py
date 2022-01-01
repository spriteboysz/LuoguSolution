#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 09:52:15
LastEditTime: 2021-10-22 09:58:42
Description: 哥德巴赫猜想
FilePath: P1304.py
'''

def func():
    n = int(input())
    lst, num, flag = [2], 3, True
    while num < n:
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

    for i in range(4, n + 2, 2):
        for j in lst:
            if (i - j) in lst:
                print("{}={}+{}".format(i, j, i - j))
                break


if __name__ == '__main__':
    func()
    