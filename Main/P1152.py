#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-22 10:04:11
LastEditTime: 2021-10-22 10:23:07
Description: 欢乐的跳
FilePath: P1152.py
'''


def func():
    # *字符+列表的接收方式
    n, *lst1 = list(map(int, input().strip().split()))

    lst2 = [1] + [0] * (n - 1)
    for i in range(n - 1):
        if abs(lst1[i] - lst1[i + 1]) < n:
            lst2[abs(lst1[i] - lst1[i + 1])] += 1
            if lst2.count(0) == 0:
                print("Jolly")
                return
    print("Not jolly")


if __name__ == '__main__':
    func()
