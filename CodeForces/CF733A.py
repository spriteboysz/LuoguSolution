#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-21 17:51:14
LastEditTime: 2021-11-21 18:05:04
Description: Grasshopper And the String
FilePath: CF733A.py
'''


def func():
    s1 = input().strip()
    vowel = ["A", "E", "I", "O", "U", "Y"]
    point = [0]
    for index, value in enumerate(s1):
        if value in vowel:
            point.append(index + 1)
    point.append(len(s1) + 1)
    ability = []
    for i in range(1, len(point)):
        ability.append(point[i] - point[i - 1])
    print(max(ability))


if __name__ == '__main__':
    func()
