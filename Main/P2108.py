#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2021-12-17 22:55:04
LastEditTime: 2021-12-17 23:21:48
Description: 学英语
FilePath: P2108.py
'''


def func():
    num1 = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
            "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    num2 = [0, 0, "twenty", "thirty", "forty", "fifty",
            "sixty", "seventy", "eighty", "ninety"]

    number = input().strip().split()
    ans, now = 0, 0
    for el in number:
        if el in num1:
            now += num1.index(el)
        elif el in num2:
            now += num2.index(el) * 10
        elif el == "hundred":
            now *= 100
        elif el == "thousand":
            ans += now * 1000
            now = 0
        elif el == "million":
            ans += 1000000 * now
            now = 0
    ans += now
    print(-ans if number[0] == "negative" else ans)


if __name__ == '__main__':
    func()
