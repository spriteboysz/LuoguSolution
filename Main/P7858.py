#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-02 21:45:59
LastEditTime: 2022-01-02 22:00:48
Description: MARKO
FilePath: P7858.py
'''


def func():
    base = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

    n = int(input())
    word, count = [], 0
    for _ in range(n):
        word.append(input().strip())
    s = input().strip()

    for item in word:
        for i in range(len(item)):
            if item[i] not in base[s[i]]:
                break
        else:
            count += 1
    print(count)


if __name__ == '__main__':
    func()
