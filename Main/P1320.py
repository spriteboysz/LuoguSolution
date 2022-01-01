#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-12 23:32:53
LastEditTime: 2021-12-09 22:55:39
Description: 压缩技术（续集版）
FilePath: P1320.py
'''


def func():
    lst = input().strip()
    n = len(lst)
    for i in range(n - 1):
        lst += input().strip()

    lst0 = list(map(len, [i for i in lst.split("1") if i != ""]))
    lst1 = list(map(len, [i for i in lst.split("0") if i != ""]))
    if lst[0] == "1":
        lst0 = [0] + lst0

    lst2 = [0] * (len(lst0) + len(lst1))
    for i in range(0, len(lst0)):
        lst2[i * 2] = lst0[i]
    for i in range(0, len(lst1)):
        lst2[i * 2 + 1] = lst1[i]
    print(str(n), " ".join(map(str, lst2)))


if __name__ == '__main__':
    func()
