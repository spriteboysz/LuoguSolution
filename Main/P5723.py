#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-08 21:23:36
Description: 质数口袋
FilePath: P5723.py
'''


def isPrime(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def func():
    l = int(input())
    if l < 2:
        print(0)
        return

    count, ssum, num = 0, 0, 2
    while ssum + num <= l:
        if isPrime(num):
            print(num)
            count += 1
            ssum += num
        num += 1
    print(count)


if __name__ == '__main__':
    func()
