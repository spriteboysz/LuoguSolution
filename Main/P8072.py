#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-24 23:09:50
LastEditTime: 2022-03-24 23:15:09
Description: COKOLADA
FilePath: P8072.py
"""


def func():
    k = int(input())
    binary = bin(k)[2:]
    length, minimum = len(binary), len(binary.rstrip("0"))
    if minimum == 1:
        print(2 ** (length - 1), 0)
    else:
        print(2 ** length, minimum)


if __name__ == "__main__":
    func()
