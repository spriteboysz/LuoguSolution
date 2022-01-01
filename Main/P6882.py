#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-05 17:17:55
LastEditTime: 2021-12-05 17:48:47
Description: Imena
FilePath: P6882.py
'''


def func():
    n = int(input())
    s = input().strip()
    sentence = list(s.replace(".", "\n").replace(
        "！", "\n").replace("?", "\n").strip().split("\n"))

    for i in range(len(sentence)):
        count = 0
        word = sentence[i].strip().split()
        for j in range(len(word)):
            if word[j].isalpha() and word[j][0].isupper() and word[j][1:].islower():
                count += 1
        print(count)


if __name__ == '__main__':
    func()
