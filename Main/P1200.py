#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-13 23:00:37
LastEditTime: 2021-10-13 23:18:41
Description: 你的飞碟在这儿
FilePath: P1200.py
'''


def number(name):
    product = 1
    for ch in name:
        product *= ord(ch) - ord("A") + 1
    return product


def func():
    comet = input().strip()
    team = input().strip()
    if number(comet) % 47 == number(team) % 47:
        print("GO")
    else:
        print("STAY")


if __name__ == '__main__':
    func()
