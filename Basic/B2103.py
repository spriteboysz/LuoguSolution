#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 00:15:06
Description: 图像相似度
FilePath: B2103.py
'''

def func():
    m, n = map(int, input().strip().split())
    lst1, lst2 = [], []
    for i in range(m):
        row = list(map(int, input().strip().split()))
        lst1.append(row)
    for j in range(m):
        row = list(map(int, input().strip().split()))
        lst2.append(row)

    count = 0
    for i in range(m):
        for j in range(n):
            if lst1[i][j] == lst2[i][j]:
                count += 1

    print("%.2f" % (count * 100 / (m * n)))


if __name__ == '__main__':
    func()
    