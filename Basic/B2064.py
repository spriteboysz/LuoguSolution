#!/user/bin/env python
# coding:   utf-8
# @Time:    2021-09-10 23:07
# @Author:  Deean
# @File:    P02_B2064

# 题目描述
# 菲波那契数列是指这样的数列：数列的第一个和第二个数都为 11，接下来每个数都等于前面 22个数之和。
# 给出一个正整数 a，要求菲波那契数列中第 a 个数是多少。
#
# 输入格式
# 第 1 行是测试数据的组数 n，后面跟着 n 行输入。每组测试数据占 1 行，包括一个正整数 a(1 \le a \le 30)a(1≤a≤30)。
#
# 输出格式
# 输出有 n 行，每行输出对应一个输入。输出应是一个正整数，为菲波那契数列中第 a 个数的大小。

# def func(aa):
#     if aa == 1:
#         return 1
#     elif aa == 2:
#         return 1
#     else:
#         return func(aa - 1) + func(aa - 2)
#
#
# nn = int(input())
# for item in range(nn):
#     print(func(int(input())))

nums = input().split(" ")
aa = int(nums[0])
bb = int(nums[1])
cc = int(nums[2])
mm = max(aa, bb, cc) / (max((aa + bb), bb, cc) * max(aa, bb, (bb + cc)))
print("%.3f" % mm)
