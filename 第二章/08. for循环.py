# for循环: 遍历输入的字符串
msg = input("请输入要遍历的字符串: ")
for s in msg: # s 表示遍历出来的元素; msg 表示需要遍历的数据
    print(f"元素: {s}")
else:
    print("遍历结束!")

# 案例1: 计算1-100之间所有的奇数之和
total = 0
# 原始版
for i in range(1, 101):
    if i % 2 == 1: # 奇数  替换原句: i % 2 != 0
        total += i
    i += 1

# 简化
for i in range(1, 101, 2):
    total += i
print(f"1-100之间所有的奇数之和: {total}")

# 案例2:计算100-500之间所有3的倍数的数字之和
total1 = 0
for i in range(100, 501):
    if i % 3 == 0: # i 是3的倍数
        total1 += i
    i += 1
print(f"100-500之间所有3的倍数的数字之和: {total1}")

"""
    嵌套循环: 根据输入的长方形的长度 m, 宽度 n, 打印一个长方形;
    如下: 是一个长度为10, 宽度为5的长方形
    * * * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *
    * * * * * * * * * *
    
    print("*"): 自带换行效果, 每一次执行都会输出新的一行中;
    print("*", end=""): end表示的是每一次输出以什么结束; 默认 \n, 表示换行.
"""
# 1. 接收键盘录入 m, n
# 长度
m = int(input("请输入长方形的长度: "))
# 宽度
n = int(input("请输入长方形的宽度: "))

# 2. 打印长方形
for j in range(n): # 控制行
    for i in range(m): # 控制列
        print("*", end="  ")
    print()


# 嵌套循环案例: 打印99乘法表
for i in range(1, 10): # 外层循环 - 控制行
    for j in range(1, i + 1): # 内层循环 - 控制列
        print(f"{j} x {i} = {j * i}", end="\t")
    print()


# 练习1: 根据输入的直角边的边长，打印等腰直角三角形（如下为直角边为5的等腰直角三角形)
# num = int(input("请输入直角边的边长: "))
# for i in range(num):
#     for j in range(i + 1):
#         print("*", end="  ")
#     print()
# 参考答案
for i in range(1, 6):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# 练习2: 根据输入的数字, 打印对应的数字金字塔
# num1 = int(input("请输入一个数字: "))
# for i in range(num1):
#     for j in range(i + 1):
#         print(f"{j + 1}", end="  ")
#     print()
# 参考答案
num = int(input("请输入数字: "))

for i in range(1, num+1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 练习3: 打印国际象棋棋盘
# for i in range(1, 9):
#     for j in range(1, 9):
#         if i % 2 != 0:
#             if j % 2 == 0:
#                 print("□", end="  ")
#             else:
#                 print("■", end="  ")
#         else:
#             if j % 2 == 0:
#                 print("■", end="  ")
#             else:
#                 print("□", end="  ")
#     print()
# 正确答案
for i in range(8):
    for j in range(8):
        if (i + j) % 2 == 0:
            print("■", end="  ")
        else:
            print("□", end="  ")
    print()
