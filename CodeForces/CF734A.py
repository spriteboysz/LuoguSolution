#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2021-11-06 14:26:30
LastEditTime: 2021-11-06 14:33:16
Description: Anton and Danik
FilePath: CF734A.py
"""


def func():
    _ = int(input())
    s = input().strip()
    anton, danik = s.count("A"), s.count("D")
    if anton > danik:
        print("Anton")
    elif anton < danik:
        print("Danik")
    else:
        print("Friendship")


if __name__ == "__main__":
    func()
