#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-20 23:25:57
LastEditTime: 2021-10-20 23:31:26
Description: 连续出现的字符
FilePath: B2126.py
'''


def func():
    k = int(input())
    s1 = input().strip()

    s2 = [1] * len(s1)
    for i in range(1, len(s1)):
        if s1[i] == s1[i - 1]:
            s2[i] = s2[i - 1] + 1
            if s2[i] >= k:
                print(s1[i])
                break
    else:
        print("No")


if __name__ == '__main__':
    func()
