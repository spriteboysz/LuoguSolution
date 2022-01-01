#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-20 23:34:23
LastEditTime: 2021-12-20 23:48:19
Description: KARTE
FilePath: P6529.py
'''


def func():
    s = input().strip()
    base = ["P", "K", "H", "T"]
    card = [[] for _ in range(4)]
    for i in range(len(s) - 2):
        if s[i] in base:
            num = int(s[i + 1] + s[i + 2])
            if num not in card[base.index(s[i])]:
                card[base.index(s[i])].append(num)
            else:
                print("GRESKA")
                break
    else:
        print(" ".join(map(lambda el: str(13 - len(el)), card)))


if __name__ == '__main__':
    func()
    