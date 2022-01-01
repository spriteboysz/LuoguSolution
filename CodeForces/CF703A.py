#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 16:34:38
LastEditTime: 2021-11-07 16:40:51
Description: Mishka and Game
FilePath: CF703A.py
'''


def func():
    n = int(input())
    games = []
    for _ in range(n):
        a, b = map(int, input().strip().split())
        if a > b:
            games.append(1)
        elif a < b:
            games.append(-1)

    if sum(games) > 0:
        print("Mishka")
    elif sum(games) < 0:
        print("Chris")
    else:
        print("Friendship is magic!^^")


if __name__ == '__main__':
    func()
