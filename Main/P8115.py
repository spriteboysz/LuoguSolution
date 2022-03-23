#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-23 22:37:57
LastEditTime: 2022-03-23 23:01:04
Description: Table
FilePath: P8115.py
"""


def func():
    nums = input().lstrip("{").rstrip("}").split(",")
    mixed = []
    for num in filter(lambda el: el != "", nums):
        hexadecimal = hex(int(num)).upper().replace("X", "x")
        if len(hexadecimal) <= len(num):
            mixed.append(hexadecimal)
        else:
            mixed.append(num)
    print("{" + ",".join(mixed) + "}")


if __name__ == "__main__":
    func()
