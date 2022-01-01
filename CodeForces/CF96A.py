#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-02 23:43:35
LastEditTime: 2021-11-02 23:46:15
Description: Football
FilePath: CF96A.py
'''


def func():
    players = input().strip()
    if players.count("0" * 7) or players.count("1" * 7):
        return "YES"
    else:
        return "NO"


if __name__ == '__main__':
    ans = func()
    print(ans)
