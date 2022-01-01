#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-20 14:23:20
LastEditTime: 2021-11-20 14:28:35
Description: Fingerprints
FilePath: CF994A.py
'''


def func():
    n, m = map(int, input().strip().split())
    password = input().strip().split()
    fingerprint = input().strip().split()
    code = []
    for item in password:
        if item in fingerprint:
            code.append(item)
    print(" ".join(code))


if __name__ == '__main__':
    func()
