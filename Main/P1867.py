#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-19 22:39:47
LastEditTime: 2021-12-19 22:59:44
Description: 【Mc生存】经验值
FilePath: P1867.py
'''

from math import log2
def func():
    n = int(input())
    life, exp = 10, 0
    for _ in range(n):
        x, a = map(float, input().strip().split())
        life = min(10, life - x)
        if life <= 0:
            break
        else:
            exp += a
    grade = int(log2(exp + 1))
    print(grade, int(exp + 1 - 2 ** grade))
        
        


if __name__ == '__main__':
    func()
    