#!/user/bin/env python
# coding:   utf-8
# @Time:    2021-09-04 12:59
# @Author:  Deean
# @File:    P02_B2012
"""
题目描述
甲流并不可怕，在中国，它的死亡率并不是很高。请根据截止 20092009 年 1212 月 2222 日各省报告的甲流确诊数 aa 和死亡数 bb，计算甲流在各省的死亡率。

输入格式
输入共两行，第一行一个整数为确诊数 aa，第二行一个整数为死亡数 bb。
"""

# s = int(input())
# d = int(input())
# print("%.3f%%" % (d / s * 100))

# nums = input().split(" ")
# for i in range(2, int(nums[0])):
#     if int(nums[0]) % i == int(nums[1]) % i and int(nums[0]) % i == int(nums[2]) % i:
#         print(i)
#         break

# count = int(input())
# nums = input().split(" ")
# print(" ".join(nums[::-1]))

# nums = input().strip().split(" ")
# a = int(nums[0])
# b = int(nums[1])
# c = int(nums[2])
# if a > b:
#     a,b = b,a
# if a > c:
#     a,c = c,a
# if b > c:
#     b,c = c,b
# print(" ".join([str(a),str(b),str(c)]))

# c = input()
# print(ord(c))

i = input().strip()
c = int(bool(int(i)))
print(c)
