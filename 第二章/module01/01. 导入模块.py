# 1. 导入模块 ---> 调用方式: 模块名.功能名 / 别名.功能名
import random
import random as rd

# 2. 导入模块中的功能 from ... import ... ---> 调用方式: 功能名 / 别名
from random import randint
from random import randint as rint
from random import * # 直接调用randint即可

for i in range(100):
    print(random.randint(1, 100))
    print(rd.randint(1, 100))

for i in range(100):
    print(randint(1, 100))
    print(rint(1, 100))
