#!/user/bin/env python
# coding:   utf-8
# @Time:    2021-09-08 23:39
# @Author:  Deean
# @File:    P02_B2601

# 题目描述
# 给定 kk（1<k<1001<k<100）个正整数，其中每个数都是大于等于 11，小于等于 1010 的数。写程序计算给定的 kk 个正整数中，11，55 和 1010 出现的次数。
#
# 输入格式
# 输入有两行：第一行包含一个正整数 kk，第二行包含 kk 个正整数，每两个正整数用一个空格分开。
#
# 输出格式
# 输出有三行，第一行为 11 出现的次数，，第二行为 55 出现的次数，第三行为 1010 出现的次数。

count = int(input())
nums = input().split(" ")
k1 = 0
k5 = 0
k10 = 0
for i in nums:
    if int(i) == 1:
        k1 += 1
    elif int(i) == 5:
        k5 += 1
    elif int(i) == 10:
        k10 += 1
print(k1)
print(k5)
print(k10)
