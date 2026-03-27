# 字典 key不能重复(如果重复, 后面的值, 会覆盖前面的值)、key必须得是不可变类型(str, int, float, tuple)
# 定义字典
from os import name

dict1 = {"王林": 670, "李慕婉": 608, "许立国": 580, "韩立": 688}
print(dict1)
print(type(dict1))

# key必须得是不可变类型(str, int, float, tuple), 不能是list, set, dict
dict2 = {0: 670, 1.5: 608, (1, 2): 580, ('A', 'B'): 688}
print(dict2)

# 访问
print(dict1["李慕婉"]) # 获取
dict1["李慕婉"] = 688 # 修改
print(dict1)


# -------------------------------------- 字典 常见操作 --------------------------------------
dict1 = {"王林": 670, "李慕婉": 608, "许立国": 580, "韩立": 688}
print(dict1)

# 添加 - key不存在就是添加
dict1["山楂"] = 550
print(dict1)

# 修改 - key存在就是修改
dict1["山楂"] = 620
print(dict1)

# 查询
print(dict1["山楂"]) # 根据key获取value
print(dict1.get("山楂")) # 根据key获取value

print(dict1.keys()) # 获取所有的key dict_keys(['王林', '李慕婉', '许立国', '韩立', '山楂'])
print(dict1.values()) # 获取所有的value dict_values([670, 608, 580, 688, 620])
print(dict1.items()) # 获取所有的键值对 key:value dict_items([('王林', 670), ('李慕婉', 608), ('许立国', 580), ('韩立', 688), ('山楂', 620)])

# 删除
score = dict1.pop("许立国")
print(score)
print(dict1)

del dict1["韩立"]
print(dict1)

# 遍历
for k in dict1.keys():
    print(f"{k} : {dict1[k]}")

for item in dict1.items():
    print(f"{item[0]} : {item[1]}")
for k, v in dict1.items():
    print(f"{k} : {v}")



"""
    案例:
    开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据,通过控制台菜单与用户交互。
    具体功能如下:
        1．添加购物车∶ 用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
        2．修改购物车∶ 要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
        3．删除购物车: 要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
        4．查询购物车: 将购物车中的商品信息展示出来，格式为:"商品名称: xxx，商品价格: xxx，商品数量: xxx"。
        5．退出购物车
        
    结构: shopping_cart = {"iphone 17": {"price": 5999, "num": 2}, "鼠标": {...}}
"""
shopping_cart = {}
# 用menu将要输出的信息存储, 再输出!!!
menu = """
########## 购物车系统 ##########
#        1. 添加购物车         #
#        2. 修改购物车         #
#        3. 删除购物车         #
#        4. 查询购物车         #
#        5. 退出购物车         #
##############################
"""

# 1. 制作菜单
print("欢迎使用购物车管理系统~")

# 2. 执行的具体操作
while True:
    print(menu)
    choice = input("请输入要执行的操作(1-5): ")
    match choice:
        case "1": # 添加购物车
            goods_name = input("请输入商品名称: ")
            goods_price = float(input("请输入商品价格: ")) # 别忘记了, 将价格转为float类型
            goods_num = int(input("请输入商品数量: ")) # 别忘记了, 将数量转为int类型

            # 这个步骤忘记了呢!!! 忘记判断商品是否存在了
            # 如果商品存在, 则不执行添加, 提示信息 (判断 goods_name 是否为字典的键)
            if goods_name in shopping_cart: # 直接用in就行了, shopping_cart不用写成shopping_cart.keys()
                print("该商品已存在, 请重新选择~")
            else:
                shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
                print("商品添加完成~")
            # continue 这句不需要, 因为会默认进入下一次循环的!!!
        case "2": # 修改购物车
            goods_name = input("请输入要修改的商品名称: ")
            # 如果商品不存在, 则提示错误信息, 重新选择
            if goods_name not in shopping_cart:
                print("该商品不存在, 请重新选择~")
                continue # 这里才要使用continue, 结束本次循环, 进入下一次循环

            goods_price = float(input("请输入商品最新的价格: "))
            goods_num = int(input("请输入商品最新的数量: "))
            shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
            print("商品修改完成~")
            # continue 这句不需要, 因为会默认进入下一次循环的!!!
        case "3": # 删除购物车
            goods_name = input("请输入要删除的商品名称: ")

            # 如果商品不存在, 则提示错误信息, 重新选择
            if goods_name not in shopping_cart:
                print("该商品不存在, 请重新选择~")
            else:
                del shopping_cart[goods_name]
                print("商品删除完成~")
            # continue 这句不需要, 因为会默认进入下一次循环的!!!
        case "4": # 查询购物车
            for goods_name in shopping_cart.keys():
                # 这一步和我自己写的不同!!!
                goods_info = shopping_cart[goods_name]
                print(f"商品名称 : {goods_name}, 商品价格: {goods_info['price']}, 商品数量: {goods_info['num']}")
            # continue 这句不需要, 因为会默认进入下一次循环的!!!
        case "5": # 退出购物车
            print("Bye~")
            break
        case _: # 匹配其他所有情况
            print("非法操作, 不支持!!!")
            # continue 这句不需要, 因为会默认进入下一次循环的!!!


"""
    练习:
    开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下:
        1．添加学生信息: 根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
        2．修改学生信息: 要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
        3．删除学生信息: 要求输入要删除的学生姓名，根据姓名删除学生信息。
        4．查询学生信息: 要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
        5．列出所有学生: 遍历所有学生信息并输出。
        6．统计班级成绩: 统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
        7．退出系统。
"""
print("欢迎进入教务管理系统~")
menu = """
# # # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # # # # #
#   1. 添加学生信息   2. 修改学生信息   3. 删除学生信息   4. 查询学生信息   5. 列出所有学生   6. 统计班级成绩   7. 退出系统   #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""
student_scores = {}
while True:
    # 1. 制作菜单
    print(menu)

    # 2. 执行具体的操作
    choice = input("请选择要执行的操作(1-7): ")
    match choice:
        case "1": # 添加学生信息
            student_name = input("请输入学生姓名: ")

            # 如果学生存在, 则不执行添加, 提示信息
            if student_name in student_scores:
                print("该学生已存在, 请重新选择~")
                # continue continue不用, 下面的语句放在else里即可
            else:
                chinese_score = float(input("请输入语文成绩: "))
                math_score = float(input("请输入数学成绩: "))
                english_score = float(input("请输入英语成绩: "))
                student_scores[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
                print(f"添加【{student_name}】成功")
        case "2": # 修改学生信息
            student_name = input("请输入要修改的学生姓名: ")

            # 如果学生不存在, 则提示错误信息, 重新选择
            if student_name not in student_scores:
                print("该学生不存在, 请重新选择~")
                continue
            chinese_score = float(input("请输入语文成绩: "))
            math_score = float(input("请输入数学成绩: "))
            english_score = float(input("请输入英语成绩: "))
            student_scores[student_name] = {"chinese": chinese_score, "math": math_score, "english": english_score}
            print(f"修改【{student_name}】成功")
        case "3": # 删除学生信息
            student_name = input("请输入要删除的学生姓名: ")

            # 如果学生不存在, 则提示错误信息, 重新选择
            if student_name not in student_scores:
                print("该学生不存在, 请重新选择~")
                # continue continue不用, 下面的语句放在else里即可
            else:
                del student_scores[student_name]
                print(f"删除【{student_name}】成功")
        case "4":
            student_name = input("请输入要查询的学生姓名: ")

            # 如果学生不存在, 则提示错误信息
            if student_name not in student_scores:
                print("该学生不存在, 请重新选择~")
                # continue continue不用, 下面的语句放在else里即可
            else:
                student_info = student_scores[student_name] # 多写一个步骤, 就不用写那么复杂了: student_scores[student_name]["math"]
                print(f"学生姓名: {student_name}, 语文成绩: {student_info["chinese"]}, 数学成绩: {student_info["math"]}, 英语成绩: {student_info["english"]}")
        case "5":
            for student_name in student_scores.keys():
                student_info = student_scores[student_name]
                print(f"学生姓名: {student_name}, 语文成绩: {student_info["chinese"]}, 数学成绩: {student_info["math"]}, 英语成绩: {student_info["english"]}")
        case "6": # 统计班级成绩
            # 忘记判断空的情况了!!!
            if not student_scores:
                print("系统中暂无学生信息, 请先添加学生~")
                continue

            # 我的总体思路是对的, 但是老师的找出最高分, 最低分的学生的细节没看明白呀??? 根据老师的思路改造一下代码!!!
            # 初始化统计变量
            chinese_scores = []
            math_scores = []
            english_scores = []

            # 收集所有成绩
            # 这里改为遍历items(), 不单独遍历keys(), 不然获取成绩麻烦呢!!!
            for student_name, scores in student_scores.items():
                chinese_scores.append(scores["chinese"])
                math_scores.append(scores["math"])
                english_scores.append(scores["english"])

            # 计算最高分、最低分、平均分
            chinese_max = max(chinese_scores)
            chinese_min = min(chinese_scores)
            chinese_avg = sum(chinese_scores) / len(chinese_scores)

            math_max = max(math_scores)
            math_min = min(math_scores)
            math_avg = sum(math_scores) / len(math_scores)

            english_max = max(english_scores)
            english_min = min(english_scores)
            english_avg = sum(english_scores) / len(english_scores)

            # 找出最高分和最低分的学生
            """ 
                怎么获得语文、数学、英语最高分和最低分的学员姓名??? 感觉可以去student_scores里查找吧, 还是不太对, 提示不能用str查找呀! 逻辑上差不多可以, 但是感觉很冗余, 看看正确写法吧!!!
                好像知道我错的地方了, 这里我只要把要查找的数据列出来就不会报错了呀, 要单独把scores列出来!!!
                !!!之前的写法 这个写法错误的点在于, 用字符串去索引字符串, 想当于"张三"["chinese"], 但是Python 规定字符串只能用整数索引
                
                为什么你会觉得两种写法一样?
                    因为你心里想的逻辑是：“遍历每个键，然后通过这个键去拿到对应的值。”
                    但在代码里，你拿着键 s 这个字符串，却没有告诉 Python 去用它作为键去查原字典。你需要的是 student_scores[s]["chinese"]，而不是 s["chinese"]。
                
                ✅ 总结
                   写法	                       原理
                  items()	直接拿到键和值，访问值直接用 scores["chinese"]
                  keys()	只拿到键，需要再用键去原字典取值：student_scores[name]["chinese"]
                你的错误版本是在 对字符串做索引，而不是 用字符串去索引字典。
                而 .items() 版本简洁、高效、不易出错，是 Python 中处理这类问题的标准写法。
            """
            # chinese_max_students = [name for s in student_scores.keys() if s["chinese"] == chinese_max] # TypeError: string indices must be integers, not 'str'
            chinese_max_students = [name for name, scores in student_scores.items() if scores["chinese"] == chinese_max]
            # scores["chinese"] 是用字符串 "chinese" 去索引字典 scores，这是合法的，取出语文成绩。 字典索引键
            chinese_min_students = [name for name, scores in student_scores.items() if scores["chinese"] == chinese_min]

            math_max_students = [name for name, scores in student_scores.items() if scores["math"] == math_max]
            math_min_students = [name for name, scores in student_scores.items() if scores["math"] == math_min]


            english_max_students = [name for name, scores in student_scores.items() if scores["english"] == english_max]
            english_min_students = [name for name, scores in student_scores.items() if scores["english"] == english_min]

            # 输出统计结果
            print("==== 班级成绩统计 ====")
            print(f"语文 - 最高分: {chinese_max}, 最低分: {chinese_min}, 平均分: {chinese_avg:.2f}")
            print(f"    最高分学生: {chinese_max_students}")
            print(f"    最低分学生: {chinese_min_students}")

            print(f"数学 - 最高分: {math_max}, 最低分: {math_min}, 平均分: {math_avg:.2f}")
            print(f"    最高分学生: {math_max_students}")
            print(f"    最低分学生: {math_min_students}")

            print(f"英语 - 最高分: {english_max}, 最低分: {english_min}, 平均分: {english_avg:.2f}")
            print(f"    最高分学生: {english_max_students}")
            print(f"    最低分学生: {english_min_students}")
            print("====================")
        case "7": # 退出系统
            print("Bye~")
            break
        case _: # 匹配其他所有情况
            print("非法操作, 不支持!!!")