# coding=utf-8
# 标识=C语言中的这个对象在计算机内存中的地址
# 例如人的身份证ID一样，每个对象都有唯一的ID标识
# 对于64位系统，一个整数两个字节32bit

num1 = 1
num2 = 2
num3 = '1'
num4 = '2'
num5 = '3'
print(id(num5))
print(id(num1))
print(id(num2))
print(id(num3))
print(id(num4))