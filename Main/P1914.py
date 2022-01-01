#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-14 22:46:58
LastEditTime: 2021-10-14 23:05:15
Description: 小书童-凯撒密码
FilePath: P1914.py
'''

import string


def func():
    n = int(input())
    pwd = input().strip()
    key = string.ascii_lowercase[n:] + string.ascii_lowercase[:n]

    plaintext = ""
    for item in pwd:
        plaintext += key[ord(item) - ord("a")]
    print(plaintext)


if __name__ == '__main__':
    func()
