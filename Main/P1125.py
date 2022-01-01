#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 13:50:44
LastEditTime: 2021-10-10 20:10:24
Description: 笨小猴
FilePath: P1125.py
'''


def isPrime(n):
    if n == 0 or n == 1:
        return False
    
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def func():
    word = input().strip()
    frequency = []
    for item in list(set(word)):
        frequency.append(word.count(item))

    if isPrime(max(frequency) - min(frequency)):
        print("Lucky Word")
        print(max(frequency) - min(frequency))
    else:
        print("No Answer")
        print(0)


if __name__ == '__main__':
    func()
