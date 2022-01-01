#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-04 22:41:10
LastEditTime: 2021-11-04 22:48:13
Description: Anton and Letters
FilePath: CF443A.py
'''


def func():
    s = list(input().lstrip("{").rstrip("}").replace(",", "").split())
    return(len(set(s)))


if __name__ == '__main__':
    print(func())
