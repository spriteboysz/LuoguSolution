#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 16:54:21
LastEditTime: 2021-11-28 17:06:05
Description: Extra-terrestrial Intelligence
FilePath: CF36A.py
'''


def func():
    with open("input.txt", "r") as f:
        n = int(f.readline())
        s = f.readline().strip("0")

    with open("output.txt", "w") as f:
        index = []
        for i in range(len(s)):
            if s[i] == "1":
                index.append(i)
        for i in range(len(index) - 2):
            if index[i + 1] - index[i] != index[i + 2] - index[i + 1]:
                f.write("NO")
                break
        else:
            f.write("YES")


if __name__ == '__main__':
    func()
