#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-06 23:07:14
Description: 买铅笔
FilePath: P1909.py
'''
import math

def func():
    nums = int(input())
    num, price, total = [0] * 3, [0] * 3, []
    for i in range(0, 3):
        num[i], price[i] = map(int, input().strip().split())
        total.append(math.ceil(nums / num[i]) * price[i])

    print(min(total))
            

if __name__ == '__main__':
    func()
    