# # 算术运算符 : + - * / // % **
# print("10 + 4 = ", 10 + 4) # 加
# print("10 - 4 = ", 10 - 4) # 减
# print("10 * 4 = ", 10 * 4) # 乘
# print("10 / 4 = ", 10 / 4) # 除 - 2.5
# print("10 // 4 = ", 10 // 4) # 整数(结果为整数) - 2
# print("10 % 4 = ", 10 % 4) # 取余/求模 - 2
# print("10 ** 4 = ", 10 ** 4) # 幂指数, 10的4次方 - 10000
#
# # 算术运算符的优先级 ---> ** --> * / // % --> + -
# print("0.1 + 10 / 4 ** 2", 0.1 + 10 / 4 ** 2)
#
# # 案例1: 要求输入两个数x与y，分别输出x+y的结果和x-y的结果
# # float(...)  ---> 将其他类型 转为 浮点数类型
# x = float(input("请输入x的值: "))
# y = float(input("请输入y的值: "))
#
# # 0.09999999999999998 --> 精度损失 ;
# # 由于计算机底层是基于二进制进行数据的存储于与处理, 二进制是无法准确地表示所有的小数, 因为涉及到浮点数的运算, 可能会损失精度
# print("x + y = ", x + y)
# print("x - y = ", x - y)
#
# # 练习1: 计算输入的三个整数的平均数
# num1 = int(input("请输入第一个数: "))
# num2 = int(input("请输入第二个数: "))
# num3 = int(input("请输入第三个数: "))
# print("三个整数的平均数为: ", (num1 + num2 + num3) / 3)
# # 参考答案:
# # num1 = int(input("请输入第一个数字: "))
# # num2 = int(input("请输入第二个数字: "))
# # num3 = int(input("请输入第三个数字: "))
# # avg_data = (num1 + num2 + num3) / 3
# # print(f"{num1}, {num2}, {num3} 这三个数的平均数为: {avg_data}")
#
# # 练习2: 要求输入梯形的上底、下底、高，然后计算梯形的面积
# num1 = float(input("请输入梯形的上底: "))
# num2 = float(input("请输入梯形的下底: "))
# h = float(input("请输入梯形的高: "))
# area = (num1 + num2) / 2 * h
# print(f"梯形的面积为: {area}")
# # 参考答案
# # top = float(input("请输入梯形的上底: "))
# # bottom = float(input("请输入梯形的下底: "))
# # height = float(input("请输入梯形的高: "))
# # print(f"梯形的面积是: {(top + bottom) * height / 2}")
#
# # 练习3: 要求输入圆的半径，然后计算圆的周长和面积 (周长: 2πr，面积：πr²)
# r = float(input("请输入圆的半径: "))
# PI = 3.14159
# print(f"圆的周长为: {2 * PI * r}, 圆的面积为: {PI * r ** 2}")
# # 参考答案
# # r = float(input("请输入圆的半径: "))
# # print(f"圆的周长是: {2 * 3.14 * r}")
# # print(f"圆的面积是: {3.14 * r ** 2}")
#
# # 练习4: 身体质量指数BMI的计算（BMI = 体重(kg) / 身高(m)²）
# weight = float(input("请输入体重, 单位kg: "))
# height = float(input("请输入身高, 单位m: "))
# print(f"身体质量指数BMI为: {weight / height ** 2}")
# # 参考答案
# # weight = float(input("请输入体重(单位kg): "))
# # height = float(input("请输入身高(单位m): "))
# # bmi = weight / height ** 2
# # print(f"BMI: {bmi}")

# # 赋值运算符: = += -= *= /= %= //= **=
# num = 85
#
# num += 10 # num = num + 10
# print("num += 10 后, num = ", num) # 95
#
# num -= 10 # num = num - 10
# print("num -= 10 后, num = ", num) # 85
#
# num *= 10 # num = num * 10
# print("num *= 10 后, num = ", num) # 850
#
# # 如果不运行下面这一句,那后面输出的值应该为整数类型,而不是浮点数类型
# num /= 10 # num = num / 10
# print("num /= 10 后, num = ", num) # 85.0
#
# num //= 10 # num = num // 10
# print("num //= 10 后, num = ", num) # 8.0
#
# num %= 3 # num = num % 3
# print("num %= 3 后, num = ", num) # 2.0
#
# num **= 3 # num = num ** 3
# print("num **= 3 后, num = ", num) # 8.0

# 比较运算符: == != > >= < <=
# print("100 == 100 吗: ", 100 == 100) # True
# print("'100' == '100' 吗: ", '100' == '100') # True
# print("100 != 100 吗: ", 100 != 100) # False
# print("100 > 100 吗: ", 100 > 100) # False
# print("100 >= 100 吗: ", 100 >= 100) # True
# print("100 < 100 吗: ", 100 < 100) # False
# print("100 <= 100 吗: ", 100 <= 100) # True

# 逻辑运算符: and or not
# 案例1: 键盘输入一个整数,判断这个数字是否在10-20之间  ---> 在: True, 不在: False
num = int(input("请输入一个整数: "))
print(f"{num}在10-20之间: ", num >= 10 and num <= 20) # and连接的条件是并且的关系, 两个条件同时成立(True), 结果才是True; 否则为False
# print(f"{num}在10-20之间: ", 10 <= num <= 20) # and连接的条件是并且的关系, 两个条件同时成立(True), 结果才是True; 否则为False

# 案例2: 键盘输入一个整数,判断这个数字是否不在10-20之间
num = int(input("请输入一个整数: "))
print(f"{num}不在10-20之间: ", num < 10 or num > 20) # or连接的条件,是或者的关系,只要其中有一个成立(True), 结果就是True; 全部不成立, 结果才是False
