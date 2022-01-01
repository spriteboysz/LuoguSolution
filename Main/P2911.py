#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-11 23:25:08
LastEditTime: 2021-10-14 23:27:27
Description: Bovine Bones G
FilePath: P2911.py
'''


def func():
    a, b, c = map(int, input().strip().split())
    # *数组index表示骰子和，数组值表示该骰子和出现的次数
    lst = [0] * (a + b + c + 1)
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            for k in range(1, c + 1):
                lst[i + j + k] += 1

    print(lst.index(max(lst)))


if __name__ == '__main__':
    func()
