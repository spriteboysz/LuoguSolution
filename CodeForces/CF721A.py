#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 21:57:32
LastEditTime: 2021-11-21 22:18:04
Description: One-dimensional Japanese Crossword
FilePath: CF721A.py
'''


def func():
    n = int(input())
    crossword = input().strip()
    encrypting = [0] * n
    for i in range(n):
        if crossword[i] == "B":
            encrypting[i] = 1

    for j in range(1, n):
        if encrypting[j] != 0:
            encrypting[j] += encrypting[j - 1]
            encrypting[j - 1] = 0
    lst = list(map(str, filter(lambda el: el > 0, encrypting)))
    print(len(lst))
    print(" ".join(lst))


if __name__ == '__main__':
    func()
