# if条件判断: 如果分数超过680, 我就去清华读书
# score = 600
# if score > 680:
#     print("欢迎你来清华读书!")
#     print("也恭喜你即将踏入精彩的大学生活")
# print("-------------------------")

# if案例: 结合前面学习的输入输出及if条件判断的知识，完成B站登录功能的实现（正确账号和密码为18888888888/666888) 。
# 正确的账号和密码
# ok_account = "18888888888"
# ok_password = "666888"
#
# # 1. 接收用户输入的账号和密码
# account = input("请输入您的B站账号: ")
# password = input("请输入您的B站密码: ")
#
# # 2. 判断账号和密码是否全部正确，如果账号和密码都正确，则登录成功，进入B站首页。
# if account == ok_account and password == ok_password:
#     print("登录成功~")
#     print("进入B站首页~")
#
# # 3. 判断账号和密码是否有错误的, 如果账号和密码有一个错误，则登录失败，提示错误信息。
# if account != ok_account or password != ok_password:
#     print("登录失败~")
#     print("账号或密码错误~")

# if案例: 结合前面学习的输入输出及if条件判断的知识，完成B站登录功能的实现（正确账号和密码为18888888888/666888) 。
# 正确的账号和密码
# ok_account = "18888888888"
# ok_password = "666888"
#
# # 1. 接收用户输入的账号和密码
# account = input("请输入您的B站账号: ")
# password = input("请输入您的B站密码: ")
#
# # 2. 判断账号和密码是否全部正确，如果账号和密码都正确，则登录成功，进入B站首页。
# if account == ok_account and password == ok_password:
#     print("登录成功~")
#     print("进入B站首页~")
# else:
#     print("登录失败~")
#     print("账号或密码错误~")

# 案例1: 根据用户输入的年份，判断这一年是闰年还是平年。
# 非整百年份，且能被4整除的年份是闰年
# 整百年份（如1900年、2000年）必须能被400整除才是闰年
# year = int(input("请输入需要判定的年份: "))
# # 如果是非整百年份，且能被4整除的年份是闰年; 整百年份, 必须能被400整除才是闰年 (能够被400整除,肯定能被100整除了呀!!!)
# if (year % 100 != 0 and year % 4 == 0) or (year % 400 == 0):
#     print(f"{year} 是闰年")
# else:
#     print(f"{year} 是平年")
#
# # 练习:
# # 1。需求1:根据用户输入的数字，判断该数字是奇数还是偶数。
# num = int(input("请输入一个数字: "))
# if num % 2 == 0:
#     print(f"{num}是偶数")
# else:
#     print(f"{num}是奇数")
#
# # 2．需求2∶根据用户输入的年龄，判断该用户是否已经成年（>=18，成年; 否则未成年)。
# age = int(input("请输入年龄: "))
# if age >= 18:
#     print(f"{age} 岁的人已成年")
# else:
#     print(f"{age} 岁的人未成年")
#
# # 3．需求3∶根据用户输入的数字，判断该数字是正数还是负数（不考虑0)。
# num2 = int(input("请输入一个数字: "))
# if num2 > 0:
#     print(f"{num2} 是正数")
# else:
#     print(f"{num2} 是负数")
#
# # 4．需求4∶根据用户输入的考试分数，判断该分数是否及格了(大于等于60就是及格了）。
# score = int(input("请输入考试分数: "))
# if score >= 60:
#     print(f"{score}分 及格了")
# else:
#     print(f"{score}分 不及格")

# if...elif...else 案例: 根据用户输入的数字，判断该数字是正数，还是负数，还是0?
# num = int(input("请输入数字: "))
# if num > 0:
#     print(f"{num} 是一个正数")
# elif num < 0:
#     print(f"{num} 是一个负数")
# else:
#     print(f"{num} 是0")

# 案例: 根据输入用户名、密码进行登录系统。
# 用户名、密码为 admin/666888或root/547527或 zhangsan/123456，则输出登录成功否则就提示用户名或密码错误
# name = input("请输入用户名: ")
# password = input("请输入密码: ")
# if name == "admin" and password == "666888":
#     print("登录成功1")
# elif name == "root" and password == "547527":
#     print("登录成功2")
# elif name == "zhangsan" and password == "123456":
#     print("登录成功3")
# else:
#     print("登录失败, 用户名或密码错误")

# 练习:
# 1. 根据输入的考试成绩，判断成绩等级。
# 大于等于85分为优秀心
# 60-85分为及格
# 否则就是不及格
# score = int(input("请输入考试分数: "))
# if score >= 85:
#     print(f"{score}分, 优秀")
# elif score >= 60:  # 更改原来的: elif 60 < score < 85
#     print(f"{score}分, 及格")
# else:
#     print(f"{score}分, 不及格")

# 2．购物折扣计算: 根据输入的购物车的商品总额，以及如下的折扣规则，计算实际应付的金额。
# 金额>= 500: 8折
# 300<=金额<500: 9折
# 100<=金额<300: 95折
# 金额<100: 无折扣
# total_price = float(input("请输入商品总额: ")) # money改为total_price, int(xxx)改为float(xxx)
# if total_price >= 500:
#     print(f"{total_price}元商品, 8折, 实际应付: {total_price * 0.8} 元")
# elif total_price >= 300: # 更改原来的: elif 300 <= money < 500:
#     print(f"{total_price}元商品, 9折, 实际应付: {total_price * 0.9} 元")
# elif total_price >= 100: # 更改原来的: elif 100 <= money < 300:
#     print(f"{total_price}元商品, 95折, 实际应付: {total_price * 0.95} 元")
# else:
#     print(f"{total_price}元商品, 无折扣, 需应付: {total_price} 元")

"""
案例: 三角形类型判断: 根据输入的三个边的边长(正整数)，判定是等边三角形、等腰三角形、普通三角形，还是不能构成三角形。
    1．构成三角形的条件: 两边之和大于第三边
    2．三角形判定规则:
    三个边都相等: 等边三角形
    两个边相等: 等腰三角形
    三个边都不相等: 普通三角形
"""
# 1. 接收输入的三角形三个边的边长
# a = int(input("请输入第一个边的边长: "))
# b = int(input("请输入第二个边的边长: "))
# c = int(input("请输入第三个边的边长: "))
#
# # 2. 判断三角形的类型 - pass是一个空语句, 起到一个语法占位的作用
# if a + b > c and b + c > a and a + c > b: # 条件成立, 构成三角形   # 更改原句: a + b > c or b + c > a or a + c > b
#     if a == b and b == c: # 更改原句 a == b and a == c
#         print(f"{a} {b} {c} 这三个边长构成等边三角形~")
#     elif a == b or b == c or a == c: # 更改原句: b == c, 应该写全!!!
#         print(f"{a} {b} {c} 这三个边长构成等腰三角形~")
#     else:
#         print(f"{a} {b} {c} 这三个边长构成普通三角形~")
# else:
#     print(f"{a} {b} {c} 这三个边长不能构成三角形!!!")


# 练习:
"""
北京市居民年度用电电费计算: 根据输入的用电度数，计算电费
· 北京市居民电费采用阶梯电价计价方式，所谓阶梯电价是指按照用户消费的电量分段定价，用电价格随用电量增加呈阶梯状逐级递增的一种电价定价机制。
· 阶梯电价规则:
    · 第一档:2880度以下，电费单价0.4883元/度。
    · 第二档:2880-4800度，电费单价0.5383元/度。
    · 第三档:4800度以上，电费单价0.7883元/度
"""
# 自己理解得太简单了, 应该是阶梯类型的计算呀!!!
# num = int(input("请输入用电度数: "))
# if num >= 4800:
#     print(f"{num}度, 第三档, 电费为{num * 0.7883}元")
# elif num >= 2880:
#     print(f"{num}度, 第三档, 电费为{num * 0.5383}元")
# else:
#     print(f"{num}度, 第三档, 电费为{num * 0.4883}元")
# 正确答案:
usage_elec = int(input("请输入用电度数: "))
# 定义阶梯电价
first_max = 2880 # 第一档上限
second_max = 4800 # 第二档上限

first_price = 0.4883 # 第一档单价
second_price = 0.5383 # 第二档单价
third_price = 0.7883 # 第三档单价

total_cost = 0.0 # 总电费
# 使用if语句进行阶梯电价计算
if usage_elec <= first_max:
    total_cost = first_price * usage_elec
elif usage_elec <= second_max:
    total_cost = first_price * first_max + second_price * (usage_elec - first_max)
else:
    total_cost = first_price * first_max + second_price * (second_max - first_max) + third_price * (usage_elec - second_max)
print(f"{usage_elec} 度的电费为: {total_cost} 元")
# 正确答案, 更加详细:
# # 使用if语句进行阶梯电价计算
# if usage_elec <= first_max:
#     # 全部在第一档
#     total_cost = usage_elec * first_price
# elif usage_elec <= second_max:
#     # 第一档部分
#     first_cost = first_max * first_price
#
#     # 第二档部分
#     second_usage = usage_elec - first_max
#     second_tier_cost = second_usage * second_price
#     total_cost = first_cost + second_tier_cost
# else:
#     # 第一档部分
#     first_cost = first_max * first_price
#
#     # 第二档部分
#     second_usage = second_max - first_max
#     second_cost = second_usage * second_price
#
#     # 第三档部分
#     third_usage = usage_elec - second_max
#     third_cost = third_usage * third_price
#     total_cost = first_cost + second_cost + third_cost