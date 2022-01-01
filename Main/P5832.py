#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-28 23:42:08
LastEditTime: 2021-12-28 23:52:45
Description: Where Am I? B 
FilePath: P5832.py
'''


def func():
    n = int(input())
    color = input().strip()
    for k in range(1, n):
        for i in range(n - k):
            for j in range(i + 1, n - i - k):
                if color[i:i+k] == color[j:j+k]:
                    flag = True
                    break
        if flag:
            break
    print(k)
                


if __name__ == '__main__':
    func()
    