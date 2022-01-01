#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-23 23:38:34
LastEditTime: 2021-11-23 23:53:04
Description: Even But Not Even
FilePath: CF1291A.py
'''


def func():
    t = int(input())
    for _ in range(t):
        n = int(input())
        num = input().strip()
        result = ""
        for i in range(n):
            if len(result) < 2:
                if int(num[i]) % 2 != 0:
                    result += num[i]
            else:
                break

        print(result if len(result) == 2 else -1)


if __name__ == '__main__':
    func()
