"""
采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下:
    1．添加购物车: 用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    2．修改购物车: 要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入。完成后修改该商品信息。
    3．删除购物车: 要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    4，查询购物车: 将购物车中的商品信息展示出来，格式为: "商品名称:xxx，商品价格:xxx，商品数量:xxx"。
    5．退出购物车
"""

# 商品类
class Goods:
    def __init__(self, name, price, num):
        # 方法信息忘记加了
        """
        初始化方法
        :param name: 商品名
        :param price: 商品价格
        :param num: 商品数量
        """
        self.name = name
        self.price = price
        self.num = num

    def __str__(self):
        return f"商品名称: {self.name}, 商品价格: {self.price}, 商品数量: {self.num}"

    # 修改商品信息 这里写的不太对呢
    # def update_info(self, name, price, num):
    #     self.name = name
    #     self.price = price
    #     self.num = num
    def update_info(self, price = None, num = None):
        if price is not None:
            self.price = price
        if num is not None:
            self.num = num

# 购物车系统类
class ShoppingCart:
    system_version = "1.0"
    system_name = "购物车管理系统" # 系统名字忘记创建了

    def __init__(self):
        self.goods_list = [] # 列表, 存储购物车中的商品信息

    # 添加商品到购物车
    def add_goods(self):
        name = input("请输入商品名称: ")

        for goods in self.goods_list:
            if goods.name == name:
                print("该商品已在购物车中，添加失败!")
                # break # 这里有问题, 忘记该怎么做了!!!, 应该用return, 而不是break, break只能跳出循环呀!!!
                return
            
        price = float(input("请输入商品价格: ")) # 没给price和num加float, int
        num = int(input("请输入商品数量: "))
        
        # 没有验证价格和数量是否有效
        if price > 0 and num > 0:
            goods = Goods(name, price, num)
            self.goods_list.append(goods)
            print("商品添加成功~")
        else:
            print("价格和数量必须为非负数!")
        
    # 修改购物车
    def update_goods(self):
        name = input("请输入要修改的商品名称: ")

        # 根据商品名称找到该商品
        for goods in self.goods_list:
            if goods.name == name:
                print(f"当前商品信息为: {goods}")

                price = float(input("请输入要修改的商品价格: ")) # 没给price和num加float, int
                num = int(input("请输入要修改的商品数量: "))

                # 没有验证价格和数量是否有效
                if price > 0 and num > 0:
                    goods.update_info(price, num)
                    print("商品信息修改成功~")
                    print(f"修改后的商品信息: {goods}")
                    # return
                else:
                    print("价格和数量必须为非负数!")
                return # 这里return代表找到了
            
        print("未找到该商品, 修改失败!")

    # 删除购物车中的商品
    def delete_goods(self):
        name = input("请输入要删除的商品名称: ")

        for goods in self.goods_list:
            if goods.name == name:
                self.goods_list.remove(goods)
                print("商品删除成功~")
                return

        print("未找到该商品, 请重新输入!")

    # 查询购物车中的所有商品 这里理解错误了, 不是查询单个特定的商品, 而是输出所有的商品信息
    def query_all_goods(self):
        # 别忘记了判空操作!!!
        if not self.goods_list:
            print("购物车为空!")
            return

        print("购物车中的商品信息: ")
        print("-" * 40)
        for goods in self.goods_list:
            print(goods)
        print("-" * 40)
        print(f"总计商品数量: {len(self.goods_list)}")

    # 运行购物车系统
    def run(self):
        # 购物车管理系统的名字, 忘记定义了, 这里要使用类属性才行
        print(f"欢迎使用{ShoppingCart.system_name}, V{ShoppingCart.system_version}")

        while True:
            print()
            print("# " * 35)
            print("#      1.添加商品  2.修改商品  3.删除商品  4.查询购物车  5.退出系统      ")
            print("# " * 35)
            print()

            my_choice = input("请输入要进行的操作(1-5): ")

            match my_choice:
                case "1": # 添加商品
                    self.add_goods()
                case "2": # 修改商品
                    self.update_goods()
                case "3": # 删除商品
                    self.delete_goods()
                case "4": # 查询购物车
                    self.query_all_goods()
                case "5": # 退出系统
                    print("感谢使用购物车管理系统, 再见!")
                    break
                case _: # 其他情况
                    print("非法操作, 请选择1-5之间的菜单功能!")

if __name__ == "__main__":
    shopping_cart = ShoppingCart()
    shopping_cart.run()