#!/user/bin/env python
# coding:   utf-8
# @Time:    2021-09-09 23:49
# @Author:  Deean
# @File:    P02_B2050

# 题目描述
# 给定三个正整数，分别表示三条线段的长度，判断这三条线段能否构成一个三角形。
#
# 输入格式
# 输入共一行，包含三个正整数，分别表示三条线段的长度，数与数之间以一个空格分开。（三条边的长度均不超过 10000）
#
# 输出格式
# 如果能构成三角形，则输出 1 ，否则输出 0。

ss = input().split(" ")
nn = list(map(lambda x: int(x), ss))
m = sorted(nn)
if m[0] + m[1] > m[2]:
    print(1)
else:
    print(0)
