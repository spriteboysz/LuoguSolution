#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-08 22:26:55
LastEditTime: 2021-12-08 22:41:40
Description: 津津的储蓄计划
FilePath: P1089.py
'''


def func():
    deposit, surplus = 0, 0
    budget = []
    for _ in range(12):
        budget.append(int(input()))
        
    for i in range(12):
        surplus += 300
        if surplus < budget[i]:
            print(-(i + 1))
            break
        else:
            surplus -= budget[i]
            div, surplus = divmod(surplus, 100)
            deposit += div * 100
    else:
        print(surplus + int(deposit * 1.2))


if __name__ == '__main__':
    func()
