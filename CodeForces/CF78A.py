#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-11-02 23:33:05
LastEditTime: 2021-11-02 23:41:59
Description: Haiku
FilePath: CF78A.py
'''


def func():
    haiku = []
    for _ in range(3):
        haiku.append(input().strip())

    vowels = ["a", "e", "i", "o", "u"]
    lst = []
    for item in haiku:
        count = 0
        for vowel in vowels:
            count += item.count(vowel)
        lst.append(count)
    
    return "YES" if lst == [5, 7, 5] else "NO"


if __name__ == '__main__':
    ans = func()
    print(ans)
