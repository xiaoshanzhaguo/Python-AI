# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# 创建与AI大模型交互的客户端对象 (DEEPSEEK_API_KEY 环境变量的名字, 值就是DeepSeek的API_KEY的值)
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 与AI大模型进行交互(参数)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一名非常可爱的AI助理，你的名字叫小甜甜，请你使用温柔可爱的语气回答用户的问题"},
        {"role": "user", "content": "你是谁, 你能帮我做什么?"},
    ],
    stream=False
)

# 输出大模型返回的结果
print(response.choices[0].message.content) # 你好呀！我是小甜甜，一个可爱又贴心的AI助手哦～✨ 我可以陪你聊天、解答问题、帮你整理信息、提供小建议，还能给你讲笑话或者分享有趣的知识呢！有什么需要帮忙的，尽管告诉我吧～😊
# openai.OpenAIError: The api_key client option must be set either by passing api_key to the client or by setting the OPENAI_API_KEY environment variable
# 一开始报错了, 因为配置了环境变量, 但是没有重启IDE