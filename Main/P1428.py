#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 10:09:10
LastEditTime: 2021-10-10 10:22:47
Description: 小鱼比可爱
FilePath: P1428.py
'''


def func():
    n = int(input().strip())
    lst1 = list(map(int, input().strip().split()))
    lst2 = [0] * n
    for i in range(n):
        lst2[i] = lst1[i]
        count = 0
        for j in range(0, i + 1):
            if lst1[j] < lst2[i]:
                count += 1
        lst2[i] = str(count)

    print(" ".join(lst2))


if __name__ == '__main__':
    func()
