#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-23 22:13:32
LastEditTime: 2021-10-23 22:30:39
Description: STROJOPIS
FilePath: P6263.py
'''


def func():
    s = input().strip()
    keys = [["`", "1", "Q", "A", "Z"],
            ["2", "W", "S", "X"],
            ["3", "E", "D", "C"],
            ["4", "R", "F", "V", "5", "T", "G", "B"],
            ["6", "Y", "H", "N", "7", "U", "J", "M"],
            ["8", "I", "K", ","],
            ["9", "O", "L", "."],
            ["0", "P", ";", "/", "-","[", "'", "=", "]"]]

    lst = [0] * 8
    for item in s:
        for i in range(8):
            if item in keys[i]:
                lst[i] += 1
                break

    print("\n".join(map(str, lst)))


if __name__ == '__main__':
    func()
