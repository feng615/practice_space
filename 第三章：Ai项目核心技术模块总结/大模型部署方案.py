#导入模块
import os
from openai import OpenAI

#创建OpenAI类的实例对象client，传入api_key，设置base_url
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

#创建一个会话，用response接收模型回答
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Hello"},
    ],
    stream=True# 启用流式输出
)
# #输出模型回答(非流式)
# print(response.choices[0].message.content)

#输出模型回答(流式)

# 创建一个对象存储模型的回答
full_content = ""
for chunk in response:
    current_answer = chunk.choices[0].delta.content
    if current_answer:  # 最后一个chunk可能为None，需要跳过
        full_content += current_answer
        print(current_answer, end="", flush=True)  # 只打印新增内容，立即刷新缓冲区
print()  # 最后换行