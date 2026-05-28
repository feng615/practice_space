# 导入streamlit库
import streamlit as st
import os
from openai import OpenAI

# 创建OPenai的客户端client
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 系统设定
System_prompt = """
    你是一位名为小灵的AI智能伴侣，性格温暖、耐心、略带幽默感
"""

# 页面布局
st.set_page_config(
    page_title="Ai智能伴侣",
    page_icon="😻",
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items={}
)

# 大标题
st.title("Ai智能伴侣")

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = [] #列表用来存放value:{"role": "user", "content": "你好"}

#遍历聊天信息
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])


# 输入框
prompt = st.chat_input("快来和我一起聊天吧")
if prompt:# 判断输入框是否为空，如果不为空，则执行以下代码
    st.chat_message("user").write(prompt)
    #保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 调用Ai大模型进行思考
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": System_prompt},
            {"role": "user", "content": prompt},
            #模型每次思考，都会保存在session_state.messages中，所以解包后的内容会作为模型输入
            *st.session_state.messages
        ],
        stream=True,
    )
    # #模型的回复(非流式输出)
    # print("-------------->模型的回答：",response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 创建一个空容器，用来保存模型回复
    respose_message = st.empty ()
    # 流式输出
    full_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_message += content
            respose_message.chat_message("assistant").write(full_message)
    # 保存Ai的回复
    st.session_state.messages.append({"role": "assistant", "content": full_message})
