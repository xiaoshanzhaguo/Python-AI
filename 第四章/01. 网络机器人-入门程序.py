import requests

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求， 获取数据
response = requests.get(target_url)

# 输出数据到控制台
print(response.text) # response是一个Response对象，可以通过.text属性获取数据