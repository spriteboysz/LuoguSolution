"""
题目描述
给定被除数和除数，求整数商及余数。此题中请使用默认的整除和取余运算，无需对结果进行任何特殊处理。

输入格式
一行，包含两个整数，依次为被除数和除数（除数非零），中间用一个空格隔开。

输出格式
一行，包含两个整数，依次为整数商和余数，中间用一个空格隔开。
"""

# num = input().split(" ")
# print(int(int(num[0]) / int(num[1])), int(num[0]) % int(num[1]))
a, b = map(int, input().strip().split())
print(a // b, a % b)
