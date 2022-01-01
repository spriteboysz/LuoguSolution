#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-26 22:04:33
LastEditTime: 2021-11-26 22:12:30
Description: Do Not Be Distracted! 
FilePath: CF1520A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        tasks = list(input().strip())
        for i in range(1, n):
            if tasks[i - 1] == tasks[i]:
                tasks[i - 1] = 0
        task = list(filter(lambda el: el != 0, tasks))
        print("YES" if len(task) == len(set(task)) else "NO")


if __name__ == '__main__':
    func()
