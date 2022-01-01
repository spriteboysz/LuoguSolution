# 题目描述
# 输入三个整数，输出最大的数。
#
# 输入格式
# 输入为一行，包含三个整数，数与数之间以一个空格分开。
#
# 输出格式
# 输出一行，包含一个整数，即最大的整数。

num = input().split(" ")
m = 0
if int(num[0]) > int(num[1]):
    m = int(num[0])
else:
    m = int(num[1])
if m < int(num[2]):
    m = int(num[2])
print(m)