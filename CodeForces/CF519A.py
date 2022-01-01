#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-06 22:02:33
LastEditTime: 2021-11-06 22:18:13
Description: A and B and chess
FilePath: CF519A.py
'''


def func():
    chess = ""
    for _ in range(8):
        chess += input().strip().replace(".", "")
        
    weight = {"Q": 9, "R": 5, "B": 3, "N": 3, "P": 1, "K": 0}
    result = sum(map(lambda el: weight[el] if el.isupper()
                     else -weight[el.upper()], list(chess)))
    if result > 0:
        print("White")
    elif result < 0:
        print("Black")
    else:
        print("Draw")


if __name__ == '__main__':
    func()
