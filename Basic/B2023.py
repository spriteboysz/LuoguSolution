#!/user/bin/env python
# coding:   utf-8
# @Time:    2021-09-08 22:57
# @Author:  Deean
# @File:    P02_B2023

# 题目描述
# 读入一个字符，一个整数，一个单精度浮点数，一个双精度浮点数，然后按顺序输出它们，并且要求在他们之间用一个空格分隔。输出浮点数时保留 66 位小数。
#
# 输入格式
# 第一行是一个字符；
# 第二行是一个整数；
# 第三行是一个单精度浮点数；
# 第四行是一个双精度浮点数。
#
# 输出格式
# 输出字符、整数、单精度浮点数和双精度浮点数，之间用空格分隔。
# a = input().strip()
# b = int(input())
# c = float(input())
# d = float(input())
# print(a, b, format(c, "f"), format(d, "f"))

a = float(input())
b = float(input())
print(a / b)
