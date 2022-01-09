#!/usr/bin/env python
# coding=utf-8
'''
Author: Deean
Date: 2022-01-09 22:26:06
LastEditTime: 2022-01-09 22:41:06
Description: [COCI 2009-2010 #2] RIMSKI
FilePath: P7773.py
'''


def count(roman):
    counter = [0] * 5
    base = ["I", "V", "X", "L", "C"]
    for item in roman:
        counter[base.index(item)] += 1
    return counter


def func():
    romans = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X",
              "XI", "XII", "XIII", "XIV", "XV", "XVI", "XVII", "XVIII", "XIX", "XX",
              "XXI", "XXII", "XXIII", "XXIV", "XXV", "XXVI", "XXVII", "XXVIII", "XXIX", "XXX",
              "XXXI", "XXXII", "XXXIII", "XXXIV", "XXXV", "XXXVI", "XXXVII", "XXXVIII", "XXXIX", "XL",
              "XLI", "XLII", "XLIII", "XLIV", "XLV", "XLVI", "XLVII", "XLVIII", "XLIX", "L",
              "LI", "LII", "LIII", "LIV", "LV", "LVI", "LVII", "LVIII", "LIX", "LX",
              "LXI", "LXII", "LXIII", "LXIV", "LXV", "LXVI", "LXVII", "LXVIII", "LXIX", "LXX",
              "LXXI", "LXXII", "LXXIII", "LXXIV", "LXXV", "LXXVI", "LXXVII", "LXXVIII", "LXXIX", "LXXX",
              "LXXXI", "LXXXII", "LXXXIII", "LXXXIV", "LXXXV", "LXXXVI", "LXXXVII", "LXXXVIII", "LXXXIX",
              "XC", "XCI", "XCII", "XCIII", "XCIV", "XCV", "XCVI", "XCVII", "XCVIII", "XCIX", "C"]

    s = input().strip()
    counter = count(s)
    for item in romans:
        if count(item) == counter:
            print(item)
            break
    else:
        print(-1)


if __name__ == '__main__':
    func()
