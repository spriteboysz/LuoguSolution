#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-13 23:22:17
LastEditTime: 2021-11-13 23:27:32
Description: Fair Game
FilePath: CF864A.py
'''


def func():
    n = int(input())
    lst = []
    for _ in range(n):
        lst.append(int(input()))
    if len(set(lst)) == 2 and lst.count(lst[0]) == len(lst) // 2:
        print("YES")
        print(list(set(lst))[0], list(set(lst))[1])
    else:
        print("NO")


if __name__ == '__main__':
    func()
