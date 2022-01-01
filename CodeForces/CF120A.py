#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 22:25:01
LastEditTime: 2021-11-28 22:30:24
Description: Elevator
FilePath: CF120A.py
'''


def func():
    with open("input.txt", "r") as f:
        gate = f.readline().strip()
        num = int(f.readline())

    with open("output.txt", "w") as f:
        if (gate == "front" and num == 1) or (gate == "back" and num == 2):
            f.write("L")
        else:
            f.write("R")


if __name__ == '__main__':
    func()
