# 获取键盘上输入的数据 -- input(...)
name = input("请输入您的姓名: ")
age = input("请输入您的年龄: ")

print(f"您的姓名是{name}, 您的年龄是{age}")

# 案例: 银行卡ATM取款
# 总金额
total = 10000
# 1. 输入密码
password = input("请输入密码: ")
print(f"密码正确, {password}")
# 2. 输入取款金额
num = input("请输入取款金额: ")
# 3. 计算余额并输出  ---> num 转为 int类型 ---> int(...)
print(f"取款后, 银行卡的余额为{total - int(num)}")

# 练习: 实现计算器功能
# 需求: 根据用户输入的两个数字，计算两个数之和，并将其输出到控制台。
num1 = input("请输入第一个数字: ")
num2 = input("请输入第二个数字: ")
print(f"两个数字之和为: {int(num1) + int(num2)}")
# 或:
num1 = int(input("请输入第一个数字: "))
num2 = int(input("请输入第二个数字: "))
print(f"{num1} + {num2} = {num1 + num2}")