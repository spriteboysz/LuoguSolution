#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-25 22:51:15
LastEditTime: 2022-03-25 23:12:19
Description: 妖梦拼木棒
FilePath: P3799.py
"""

from collections import defaultdict


def func():
    n = int(input())
    sticks = list(map(int, input().strip().split()))
    stickcount = defaultdict(int)
    for stick in sticks:
        stickcount[stick] += 1

    count = 0
    key = list(stickcount.keys())
    for i in range(len(key)):
        for j in range(i, len(key)):
            if key[i] + key[j] in stickcount:
                if i == j:
                    count += (stickcount[key[i]] - 1) * (
                        stickcount[key[i] + key[j]] // 2
                    )
                else:
                    count += (
                        stickcount[key[i]]
                        * stickcount[key[j]]
                        * (stickcount[key[i] + key[j]] // 2)
                    )
    print(count % (10 ** 9 + 7))


if __name__ == "__main__":
    func()
