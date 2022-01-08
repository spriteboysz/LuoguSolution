#! /usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-10-10 14:01:19
LastEditTime: 2022-01-08 23:09:22
Description: 统计单词数
FilePath: P1308.py
'''


def func():
    word = input().strip().lower()
    sentence = input().lower()
    sentences = sentence.split()
    if word in sentences:
        count = sentences.count(word)
        if sentences.index(word) == 0:
            index = sentence.find(word + " ")
        elif sentences.index(word) == len(sentences) - 1:
            index = len(sentence) - len(word) + 1
        else:
            index = sentence.find(" " + word + " ") + 1
        print(count, index)
    else:
        print(-1)


if __name__ == '__main__':
    func()
