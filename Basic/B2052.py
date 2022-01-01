#!/user/bin/env python
# coding:   utf-8
# @Time:    2021-09-10 22:47
# @Author:  Deean
# @File:    P02_B2052

# 题目描述
# 一个最简单的计算器，支持 +,-,*,/ 四种运算。仅需考虑输入输出为整数的情况，数据和运算结果不会超过 int 表示的范围。然而：
# 如果出现除数为 0 的情况，则输出：Divided by zero!。
# 如果出现无效的操作符（即不为 +,-,*,/ 之一），则输出：Invalid operator!。
#
# 输入格式
# 输入只有一行，共有三个参数，其中第 1,2个参数为整数，第 3个参数为操作符（+,-,*,/）。
#
# 输出格式
# 输出只有一行，一个整数，为运算结果。然而：

# lst = input().split(" ")
# aa = int(lst[0])
# bb = int(lst[1])
# ff = str(lst[2])
# if ff == "+":
#     print(aa + bb)
# elif ff == "-":
#     print(aa - bb)
# elif ff == "*":
#     print(aa * bb)
# elif ff == "/" and bb == 0:
#     print("Divided by zero!")
# elif ff == "/":
#     print(aa / bb)
# else:
#     print("Invalid operator!")


nn = int(input())
ss = 0
for item in range(nn):
    ss += int(input())
avg = ss / nn
print("%d %.5f" %(ss, avg))
