#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 22:24:10
LastEditTime: 2021-11-05 22:27:14
Description: Way Too Long Words
FilePath: CF71A.py
'''


def func():
    n = int(input())
    for _ in range(n):
        word = input().strip()
        if len(word) <= 10:
            print(word)
        else:
            print(word[0] + str(len(word) - 2) + word[-1])


if __name__ == '__main__':
    func()
