#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-28 15:43:48
LastEditTime: 2021-11-28 16:50:20
Description: Coins
FilePath: CF47B.py
'''


def func():
    coins = [list(input().strip()), list(
        input().strip()), list(input().strip())]
    for i in range(len(coins)):
        if "<" in coins[i]:
            coins[i][0], coins[i][2] = coins[i][2], coins[i][0]
            
    if coins[0][0] == coins[1][0]:
        print(coins[2][2] + coins[2][0] + coins[0][0])
    elif coins[1][0] == coins[2][0]:
        print(coins[0][2] + coins[0][0] + coins[1][0])
    elif coins[0][0] == coins[2][0]:
        print(coins[1][2] + coins[1][0] + coins[2][0])
    else:
        print("Impossible")


if __name__ == '__main__':
    func()
