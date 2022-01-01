#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-07 23:23:10
LastEditTime: 2021-11-07 23:43:02
Description: 
FilePath: CF255A.py
'''


def func():
    n = int(input())
    exercises = list(map(int, input().strip().split()))
    count = {"chest": 0, "biceps": 0, "back": 0}
    for i in range(n):
        if i % 3 == 0:
            count["chest"] += exercises[i]
        elif i % 3 == 1:
            count["biceps"] += exercises[i]
        else:
            count["back"] += exercises[i]

    maximum = -1
    for k, v in count.items():
        if v > maximum:
            name, maximum = k, v
    print(name)


if __name__ == '__main__':
    func()
