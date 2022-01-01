#!/user/bin/env python
# coding:   utf-8
# @Time:    2021-09-08 23:07
# @Author:  Deean
# @File:    P02_B2026

# 题目描述
# 计算两个双精度浮点数 aa 和 bb 的相除的余数，aa 和 bb 都是双精度浮点数。这里余数（rr）的定义是：a=k \times b+ra=k×b+r，其中 kk 是整数，0 \le r<b0≤r<b。
#
# 输入格式
# 输入仅一行，包括两个双精度浮点数 aa 和 bb。
#
# 输出格式
# 输出也仅一行，a/ba/b 的余数。
# num = input().split(" ")
# aa = float(num[0])
# bb = float(num[1])
# kk = int(aa / bb)
# rr = aa - kk * bb
# print(rr)

#
# s = input().strip()
# print("YES" if ord(s) % 2 != 0 else "NO")

nums = input().split()
xx = int(nums[0])
yy = int(nums[1])
print("yes" if (-1 <= xx <= 1 and -1 <= yy <= 1) else "no")
