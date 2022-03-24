#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-24 23:35:32
LastEditTime: 2022-03-24 23:37:38
Description: KINO
FilePath: P8080.py
"""


def func():
    n, seats = int(input()), input().strip().replace("LL", "S")
    print(min(n, len(seats) + 1))


if __name__ == "__main__":
    func()
