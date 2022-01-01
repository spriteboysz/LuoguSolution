#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 10:56:57
LastEditTime: 2021-10-10 13:38:46
Description: 梦中的统计 
FilePath: P1554.py
'''


def func():
    m, n = map(int, input().strip().split())
    lst1 = ""
    lst2 = [0] * 10
    for i in range(m, n + 1):
        lst1 += str(i)

    for j in range(10):
        lst2[j] += lst1.count(str(j))

    print(" ".join(map(str, lst2)))


if __name__ == '__main__':
    func()
