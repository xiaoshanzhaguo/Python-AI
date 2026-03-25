# for循环: 遍历输入的字符串
# msg = input("请输入要遍历的字符串: ")
# for s in msg: # s 表示遍历出来的元素; msg 表示需要遍历的数据
#     print(f"元素: {s}")
# else:
#     print("遍历结束!")

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
