#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 23:34:56
LastEditTime: 2021-11-28 23:46:55
Description: cAPS lOCK
FilePath: CF131A.py
'''


def func():
    word = input().strip()
    if word[1:].isupper() or len(word) == 1:
        initial = word[0].lower() if word[0].isupper() else word[0].upper()
        print(initial + word[1:].lower())
    else:
        print(word)


if __name__ == '__main__':
    func()
