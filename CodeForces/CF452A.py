#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-29 23:09:51
LastEditTime: 2021-11-29 23:17:21
Description: Eevee
FilePath: CF452A.py
'''


def func():
    pokemons = ["vaporeon", "jolteon", "flareon", "espeon",
                "umbreon", "leafeon", "glaceon", "sylveon"]
    n = int(input())
    s = input().strip()
    for item in pokemons:
        if n == len(item):
            for i in range(n):
                if s[i] != "." and s[i] != item[i]:
                    break
            else:
                print(item)
                break


if __name__ == '__main__':
    func()
