# 定义类 ----> 不推荐 动态地为对象添加属性
class Car:
    pass

# 创建对象
c1 = Car()
# 动态地为对象添加属性
c1.color = "red"
c1.brand = "BMW"
c1.name = "X5"
c1.price = 500000

print(c1)
print(c1.brand)
print(c1.__dict__) # 会将对象中的所有属性以字典的形式输出出来


# 定义类
class Car:
    # __init__ 方法是初始化的方法, 会在对象创建时自动调用, 可以在该方法中为对象设置对应的属性;
    # self: 是第一个参数, 表示当前所创建出来的实例对象
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕, 对象属性已经添加完毕 .")

# 创建对象
c1 = Car("red", "BMW", "X7", 800000)
print(c1.__dict__)

# c2 = Car() # 不传参数就会报错 TypeError: Car.__init__() missing 4 required positional arguments: 'c_color', 'c_brand', 'c_name', and 'c_price'
# print(c2.__dict__)

c2 = Car("white", "奔驰", "E300", 450000)
print(c2.__dict__)


# ----------------------------------------- 定义类 实例方法 -----------------------------------------
class Car:
    def __init__(self, c_color, c_brand, c_name, c_price):
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        print("Car 类型的对象初始化完毕, 对象属性已经添加完毕 .")

    # 定义实例方法
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中...")

    def total_price(self, discount, rate = 0.1):
        """
        计算汽车的总费用, 包含两个部分: 车的价格, 税费
        :param discount: 折扣
        :param rate: 税率
        :return: 提车的总费用
        """
        total_cost = self.price * discount + rate * self.price
        return total_cost

# 测试
c1 = Car("red", "BMW", "X7", 800000)

# 调用对象中的方法
c1.running()

total1 = c1.total_price(0.9, 0.1)
print("提车的总费用为: ", total1)

total2 = c1.total_price(0.9)
print("提车的总费用为: ", total2)