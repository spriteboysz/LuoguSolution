#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 14:01:19
LastEditTime: 2021-10-10 14:32:20
Description: 统计单词数
FilePath: P1308.py
'''


def func():
    word = input().strip().lower()
    sentence = input().strip().lower().split()
    if word in sentence:
        l = 0
        for i in range(0, sentence.index(word)):
            l += (len(sentence[i]) + 1)
        print(sentence.count(word), l + 1)
    else:
        print(-1)


if __name__ == '__main__':
    func()
