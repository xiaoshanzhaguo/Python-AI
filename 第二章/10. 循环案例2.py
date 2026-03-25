"""
    案例2: 猜数字游戏
        1．系统随机生成一个随机数
        2．用户根据提示猜数字，并将所猜的数字输入系统
        3．如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字4.如果猜对，系统自动退出，游戏结束
"""
import random
random_num = random.randint(1, 100) # 生成随机数
while True:
    # 接收输入的数字
    num = int(input("请输入一个数字(1-100): "))
    # 比较
    if num > random_num:
        print("您输入的数字太大了!")
        # continue  这里其实不需要!!!
    elif num < random_num:
        print("您输入的数字太小了!")
        # continue
    else:
        print("恭喜您, 猜对了, 666")
        break

# 练习1: 将1-1000之间(含1000）所有的5的倍数的数字累加起来。
total = 0
for i in range(1, 1001):
    if i % 5 == 0:
        total += i
print(f"1-1000 5的倍数数字之和:  {total}") # 或参考答案: print("1-1000 5的倍数数字之和: ", total)

# 练习2: 统计字符串 "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"字符串中有多少个a和k。
# s = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
# total_a = 0
# total_k = 0
# for c in s:
#     if c == "a":
#         total_a += 1
#     elif c == "k":
#         total_k += 1
# print(f"{s}字符串中, 有{total_a}个a, {total_k}个k")
# 正确答案
total = 0
for i in "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd":
    if i == "a" or i == "k":
        total += 1
print("字符串中a和k出现的次数: ", total)