#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-15 23:22:57
LastEditTime: 2021-11-15 23:30:56
Description: Зингер | color
FilePath: CF1531A.py
'''


def func():
    color, state = "blue", "unlock"
    n = int(input())
    for _ in range(n):
        command = input().strip()
        if command == "lock":
            state = "lock"
        elif command == "unlock":
            state = "unlock"
        elif state == "unlock":
            color = command
        else:
            pass
        
    print(color)


if __name__ == '__main__':
    func()
