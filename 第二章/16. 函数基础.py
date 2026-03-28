# 注意: 函数定义的时候并不会执行, 只有在调用的时候, 函数体的逻辑才会执行; 函数先定义, 后调用;
# 函数定义
def out_line():
    print("------------------------------------")
    print("------------------------------------")

# 函数调用
out_line()
out_line()
out_line()

# 函数的参数与返回值
# 函数1: 计算圆的面积
def circle_area(r):
    area = 3.14 * r ** 2
    return area

area = circle_area(10)
print(area)

# 函数2: 计算长方形的面积
def rectangle_area(l, w):
    """
    根据长方形的长度和宽度, 计算长方形的面积
    :param l: 长度
    :param w: 宽度
    :return: 长方形的面积
    """
    area = l * w
    return area

# help(rectangle_area)
print(rectangle_area(20, 10))

# 函数3: 计算圆的面积, 周长 -- 半径  ----> 如果返回值有多个, 多个返回值之间用逗号分隔 ---> 多个返回值会封装到元组之中
def circle_area_len(r):
    """
    根据圆的半径, 计算圆的面积和周长
    :param r: 半径
    :return: 圆的面积, 圆的周长
    """
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)

al = circle_area_len(10)
print(al)
print(type(al))

area, l = circle_area_len(10) # 解包
print(area)
print(type(area))


# 函数的嵌套使用
def function_a():
    print("a ... before")
    function_b()
    print("a ... after")

def function_b():
    print("b ... before")
    function_c()
    print("b ... after")

def function_c():
    print("c ...")

function_a()
print("函数调用完毕~")


# 案例1: 定义一个函数: 根据传入的底和高计算三角形面积的函数（三角形面积 = 底 * 高 / 2)
def triangle_area(b, h):
    """
    根据传入的底和高计算三角形面积
    :param b: 底长
    :param h: 高
    :return: 三角形面积
    """
    return b * h / 2
print("底长为 30, 高度为 20 的三角形面积为: ", triangle_area(30, 20))

# 案例2: 定义一个函数: 计算传入的字符串中元音字母的个数（元音字母为aeiouAEIOU)。
def count_aeiou(s): # helloworld
    """
    统计字符串中元音字母的个数
    :param s: 字符串
    :return: 元音字母的个数
    """
    num = 0
    for w in s:
        if w in "aeiouAEIOU":
            num += 1
    # for c in vowel:  老师的逻辑更好理解!!!, 在上方
    #     if c in s:
    #         num += 1
    return num
print(count_aeiou("Hello Python Hello World OK"))

# 案例3: 定义一个函数: 计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
def calc_score(score_list):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分
    :param score_list: 分数列表
    :return: 最高分, 最低分, 平均分
    """
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list), 1) # 忘记保留1位小数了
    return max_s, min_s, avg_s
s_list = [589, 609, 605, 643, 677, 455, 477, 489, 503]
max_score, min_score, avg_score = calc_score(s_list)
print("最高分: ", max_score)
print("最低分: ", min_score)
print("平均分: ", avg_score)

"""
    练习1: 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
          分数>= 90: A
          分数>= 75: B
          分数>= 60: C
          分数<60: D
"""
def get_grade(score):
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"
print(get_grade(90))
print(get_grade(80))
print(get_grade(65))
print(get_grade(40))

# 2．定义一个函数，用于判断一个字符串是否是回文串，返回bool值。
# 把字符串反转，如果和原字符串相同，就是回文串。(如: "level", "radar"，"黄山落叶松叶落山黄")
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("level"))
print(is_palindrome("hello"))
print(is_palindrome("黄山落叶松叶落山黄"))
print(is_palindrome("12321"))
print(is_palindrome("12345"))

# 3．定义一个函数: 完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def transform(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds_remain = (seconds % 3600) % 60 # second = seconds % 60 ai的写法
    return f"{seconds} 转换为 {hours} 小时 {minutes} 分钟 {seconds_remain} 秒" # return hour, minute, second
print(transform(3772))

# 4，定义一个函数: 根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形)。
def triangle_type(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        if a == b == c: # if a == b and b == c:
            return "等边三角形"
        elif a == b or a == c or b == c: # elif a == b or b == c or c == a:
            return "等腰三角形"
        else:
            return "普通三角形"
    else:
        return "不能构成三角形"
print(triangle_type(3, 4,5))
print(triangle_type(3, 5,5))
print(triangle_type(3, 4,6))
print(triangle_type(3, 5,6))
print(triangle_type(3, 4,7))
print(triangle_type(8, 8, 8))