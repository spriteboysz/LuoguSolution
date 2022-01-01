#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 10:34:51
LastEditTime: 2021-10-10 10:47:26
Description: 校门外的树
FilePath: P1047.py
'''


def func():
    l, m = map(int, input().strip().split())
    lst1 = []
    for i in range(m):
        row = list(map(int, input().strip().split()))
        lst1.append(row)

    lst2 = [1] * (l + 1)
    for i in range(m):
        for j in range(lst1[i][0], lst1[i][1] + 1):
            lst2[j] = 0
    print(lst2.count(1))


if __name__ == '__main__':
    func()
