#!/user/bin/env python
# coding:   utf-8
# @Time:    2021-09-08 22:45
# @Author:  Deean
# @File:    P02_B2024

# 题目描述
# 读入一个双精度浮点数，分别按输出格式 %f ，%f 保留 55 位小数，%e 和 %g 的形式输出这个整数，每次在单独一行上输出。
#
# 输入格式
# 一个双精度浮点数。
#
# 输出格式
# 第一行是按 %f 输出的双精度浮点数；
# 第二行是按 %f 保留 55 位小数输出的双精度浮点数；
# 第三行是按 %e 输出的双精度浮点数；
# 第四行是按 %g 输出的双精度浮点数。

f = float(input())
print(format(f, "f"))
print("%.5f" % f)
print(format(f, "e"))
print(format(f, "g"))


