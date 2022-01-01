#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-20 22:12:45
LastEditTime: 2021-10-20 22:18:18
Description: 石头剪子布
FilePath: B2112.py
'''


def func():
    n = int(input())

    gestures = ["Rock", "Scissors", "Paper"]
    for _ in range(n):
        s1, s2 = input().strip().split()
        result = gestures.index(s1) - gestures.index(s2)
        if result == 0:
            print("Tie")
        elif result == -1 or result == 2:
            print("Player1")
        else:
            print("Player2")


if __name__ == '__main__':
    func()
