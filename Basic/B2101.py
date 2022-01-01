#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-09 23:52:09
Description: 计算矩阵边缘元素之和
FilePath: B2101.py
'''

def func():
    m, n = map(int, input().strip().split())
    lst = []
    for i in range(m):
        row = list(map(int, input().strip().split()))
        lst.append(row)
    if m == 1:
        ssum = sum(lst[0])
    else:
        ssum = sum(lst[0]) + sum(lst[-1])
    for i in range(1, m - 1):
        if n == 1:
            ssum += lst[i][0]
        else:
            ssum += lst[i][0] + lst[i][-1]

    print(ssum)

     
if __name__ == '__main__':
    func()
    