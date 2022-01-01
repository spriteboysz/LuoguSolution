#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-14 23:45:20
LastEditTime: 2021-12-14 23:45:20
Description: FUNGHI
FilePath: P7659.py
'''


def func():
    pizza = []
    for _ in range(8):
        pizza.append(int(input()))
    pizza.extend(pizza)
    maximum = 0
    for i in range(8):
        current = sum(pizza[i:i + 4])
        if current > maximum:
            maximum = current
    print(maximum)


if __name__ == '__main__':
    func()
