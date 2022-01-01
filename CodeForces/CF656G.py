#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-01 22:05:10
LastEditTime: 2021-12-01 22:31:46
Description: You're a Professional
FilePath: CF656G.py
'''


def func():
    friend, item, threshold = map(int, input().strip().split())
    opinions = []
    for _ in range(friend):
        opinions.append(list(input().strip()))
        
    enjoy = list(map(lambda el: el.count("Y"), list(zip(*opinions))))
    print(len(list(filter(lambda el: el >= threshold, enjoy))))


if __name__ == '__main__':
    func()
