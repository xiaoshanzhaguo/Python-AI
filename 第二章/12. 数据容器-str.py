# 字符串 基本操作  ---> 不可变的(无法修改)、有序性、可迭代性
s = "Hello-Python"
print(s[4]) # 正向索引
print(s[-8]) # 反向索引

# s[4] = "X"
# print(s)

for i in s:
    print(i)

# 切片
print(s[0:5:1])
print(s[:5:1])
print(s[:5:])
print(s[:5])

print(s[6:12:1])
print(s[6::1])

print("-----------------------------------")

# 步长 ---> 正数: 从前往后截取; 负数: 从后往前截取
# print(s[0:5:-1]) # 方向冲突
print(s[-1:-7:-1])
print(s[::-1]) # 反转整个字符串


# ------------------------------------- 字符串常用方法 -------------------------------------
s = "     Hello-Python-Hello-World     "

# find() 查找指定字符串第一次出现的索引位置
index = s.find("-")
print(index)

# count() 统计子字符串在指定字符串中出现的次数
c = s.count("o")
print(c)

# upper() 转为大写
su = s.upper()
print(su)

# lower() 转为小写
sl = s.lower()
print(sl)

# split() 将字符串按照指定字符串切割 - 列表
slist = s.split("-")
print(slist)

# strip() 去除字符串两端的空格
ss = s.strip()
print(ss)

# replace() 将字符串中的指定子串替换为新的内容
sr = s.replace("-", "_")
print(sr)

# startswith() / endswith() 判断字符串是否是以指定的字符串开头 / 结尾, 返回布尔值
print(s.startswith("Hello"))
print(s.endswith("Python"))

print("---------------------------------")
print(s)

# ------------------------------------- 字符串案例 -------------------------------------
# 案例1: 邮箱格式验证∶ 用户输入一个邮箱，验证邮箱格式是否正确(包含一个@和至少一个.)，如果输入正确，输出"邮箱格式正确"，否则输出"邮箱格式错误"。
# 方式一:
# 1. 接收用户输入的邮箱
mail = input("请输入邮箱: ")
if mail.count("@") == 1 and mail.count(".") >= 1: # mail.find("@") != -1 不对, 要只有一个!!!
    print(f"{mail} 是合法的邮箱")                   # mail.find(".) != -1 不对, 用count()方法即可, 判断数量是否大于等于1
else:
    print(f"{mail} 是非法的邮箱")
# 判断邮箱的格式

# 方式二: in 运算符 ---> 判断子串是否存在字符串中, 存在, 返回True; 否则, 返回False
# 1. 接收用户输入的邮箱
mail = input("请输入邮箱: ")
# 判断邮箱的格式
if mail.count("@") == 1 and "." in mail:
    print(f"{mail} 是合法的邮箱")
else:
    print(f"{mail} 是非法的邮箱")


# ------------------------------------- 字符串练习 -------------------------------------
# 练习1．输入一个字符串，判断该字符串是否是回文(两边对称)。
# 黄山落叶松叶落山黄
# 上海自来水来自海上
# 感觉还是不太会??? 怎么区分偶数和奇数的字符串呢? 123怎么判断呢? 感觉不太对呢?
# s = input("请输入一个字符串: ")
# if len(s) % 2 == 0:
#     half_len = int(len(s) / 2)
# else:
#     half_len = int(len(s) / 2) - 1
# for i in range(half_len):
#     if s[i] != s[-i - 1]:
#         print(f"{s} 不是回文字符串")
#         break
#     if i == half_len - 1: print(f"{s} 是回文字符串")
# 正确答案:
s = input("请输入一个字符串: ")
# 方式一(双指针法): 思路是从两边向中间遍历, 基于索引获取两边字符对比, 如果两边的字符不相等, 则不是回文, 否则是回文。
left = 0 # 左索引
right = len(s) - 1 # 右索引
flag = True
while left < right:  # 注意这里的条件!!!
    if s[left] != s[right]:
        flag = False
        break  # 这个别忘记了!!!
    left += 1
    right -= 1
if flag:
    print(f"'{s}' 是回文")
else:
    print(f"'{s}' 不是回文")

#  方式二:
if s == s[::-1]:
    print(f"'{s}' 是回文")
else:
    print(f"'{s}' 不是回文")

# 练习2．将用户输入的10个字符串，反转后全部转换为大写，然后记录在列表中，最后将列表内容，遍历输出出来。
s_list = []
for i in range(10):
    s = input("请输入一个字符串: ")
    s_list.append(s[::-1].upper())
print("输入的字符串列表为:", s_list)
print("---------------------------------")
print("反转后的字符串列表为: ") # 忘记遍历输出了!!!
for s in s_list:
    print(s)
