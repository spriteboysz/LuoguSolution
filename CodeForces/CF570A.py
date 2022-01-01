#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-30 23:39:33
LastEditTime: 2021-11-30 23:58:53
Description: Elections
FilePath: CF570A.py
'''


def func():
    m, n = map(int, input().strip().split())
    vote = []
    for i in range(n):
        city = list(map(int, input().strip().split()))
        vote.append(city.index(max(city)) + 1)
    votes = []
    for item in set(vote):
        votes.append([item, vote.count(item)])
    print(max(votes, key=lambda el:el[1])[0])


if __name__ == '__main__':
    func()
    