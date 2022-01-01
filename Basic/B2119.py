#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-09 23:45:27
Description: 删除单词后缀
FilePath: B2119.py
'''


def func():
    word = input().strip()
    for post in ["er", "ly", "ing"]:
        if word.endswith(post):
            print(word[:(0 - len(post))])


if __name__ == '__main__':
    func()
