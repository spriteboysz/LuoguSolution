#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-17 21:55:59
LastEditTime: 2021-12-17 22:03:04
Description: 单词分类
FilePath: P1808.py
'''


def func():
    n = int(input())
    words = []
    for _ in range(n):
        word = sorted(input().strip())
        words.append("".join(word))
    print(len(set(words)))


if __name__ == '__main__':
    func()
