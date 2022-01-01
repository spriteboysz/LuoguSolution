#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 15:56:10
LastEditTime: 2021-11-28 15:58:18
Description: Numbers Joke
FilePath: CF784A.py
'''


def func():
    a = int(input())
    smith = [4, 22, 27, 58, 85, 94, 121, 166, 202, 265, 274, 319, 346, 355, 378, 382, 391, 438, 454, 483, 517, 526, 535, 562, 576,
             588, 627, 634, 636, 645, 648, 654, 663, 666, 690, 706, 728, 729, 762, 778, 825, 852, 861, 895, 913, 915, 922, 958, 985, 1086]
    print(smith[a - 1])


if __name__ == '__main__':
    func()
