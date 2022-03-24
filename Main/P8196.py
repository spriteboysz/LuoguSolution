#! /usr/bin/env python
# coding=utf-8
"""
Author: Deean
Date: 2022-03-23 23:59:51
LastEditTime: 2022-03-24 00:05:28
Description: 三元组
FilePath: P8196.py
"""


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        nums = list(map(int, input().strip().split()))
        count = 0
        for i in range(n):
            for j in range(i, n):
                if nums[i] + nums[j] in nums[j:]:
                    count += 1
        print(count)


if __name__ == "__main__":
    func()
