#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-19 23:05:48
LastEditTime: 2021-12-19 23:23:05
Description: 三子棋I
FilePath: P1838.py
'''


def func():
    win = ["123", "456", "789", "147", "258", "369", "159", "357"]
    s = input().strip()
    a, b = s[0::2], s[1::2]
    for item in win:
        if item[0] in a and item[1] in a and item[2] in a:
            print("xiaoa wins.")
            break
        elif item[0] in b and item[1] in b and item[2] in b:
            print("uim wins.")
            break
    else:
        print("drew.")


if __name__ == '__main__':
    func()
