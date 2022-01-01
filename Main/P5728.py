#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-10-15 23:29:42
LastEditTime: 2021-10-15 23:37:13
Description: 旗鼓相当的对手
FilePath: P5728.py
"""


def compete(lst1, lst2):
    for i in range(len(lst1)):
        if abs(lst1[i] - lst2[i]) > 5:
            return False
    if abs(sum(lst1) - sum(lst2)) > 10:
        return False
    else:
        return True


def func():
    num = int(input())
    lst = []
    for _ in range(num):
        row = list(map(int, input().strip().split()))
        lst.append(row)

    count = 0
    for i in range(num - 1):
        for j in range(i + 1, num):
            if compete(lst[i], lst[j]):
                count += 1

    print(count)


if __name__ == "__main__":
    func()
