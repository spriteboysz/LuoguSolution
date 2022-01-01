#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-26 17:42:43
LastEditTime: 2021-12-26 22:54:33
Description: MOBITEL 
FilePath: P6401.py
'''


def func():
    base = {"a": 2, "b": 22, "c": 222, "d": 3, "e": 33, "f": 333,
            "g": 4, "h": 44, "i": 444, "j": 5, "k": 55, "l": 555,
            "m": 6, "n": 66, "o": 666, "p": 7, "q": 77, "r": 777, "s": 7777,
            "t": 8, "u": 88, "v": 888, "w": 9, "x": 99, "y": 999, "z": 9999}
    key = list(map(int, input().strip().split()))
    s = input().strip()

    origin, current = "", ""
    for item in s:
        if len(origin) and str(base[item])[0] == origin[-1]:
            origin += "#"
        origin += str(base[item])

    for item in origin:
        if item == "#":
            current += "#"
        else:
            current += str(key.index(int(item)) + 1)
    print(current)


if __name__ == '__main__':
    func()
