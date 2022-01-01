#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-05 22:12:58
LastEditTime: 2021-11-05 22:12:59
Description: String Task
FilePath: CF118A.py
'''


def func():
    word1 = input().strip().lower()
    vowels = ["a", "o", "y", "e", "u", "i"]
    word2 = ""
    for item in word1:
        if item not in vowels:
            word2 += "." + item
    print(word2)


if __name__ == '__main__':
    func()
