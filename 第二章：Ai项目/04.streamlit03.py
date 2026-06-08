# 导入streamlit库
import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json


#保存会话信息的函数
def save_session():
    # 格式化
    if st.session_state.current_session:
        session_data = {
            "nick_name": st.session_state.nick_name,
            "character": st.session_state.character,
            "current_session": st.session_state.current_session,
            "messages": st.session_state.messages
        }

        # 如果session文件不存在，则创建文件
        if not os.path.exists("sessions"):
            os.mkdir("sessions")

        # 保存会话信息
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            print("------->会话标识：",st.session_state.current_session)
            json.dump(session_data, f, ensure_ascii=False, indent=4)


#加载所有的会话信息
def load_sessions():
    #创建一个空列表
    file_list = []
    if os.path.exists("sessions"):
        file_list = os.listdir("sessions")
        for filename in file_list:
            if filename.endswith(".json"):
               file_list.append(filename[:-5])
    return file_list


#保存当前时间的函数
def save_current_time():
        return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = [] #列表用来存放value:{"role": "user", "content": "你好"}

# 初始化昵称
if "nick_name" not in st.session_state:
    st.session_state.nick_name = "小灵"

# 初始化性格
if "character" not in st.session_state:
    st.session_state.character = "活泼开朗的台湾姑娘"

#初始化会话信息
if "current_session" not in st.session_state:
    st.session_state.current_session = save_current_time()

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

#左侧的侧边栏
with st.sidebar:
    #会话信息
    st.subheader("Ai控制面板")

    if st.button("新建会话",width="stretch",icon="✏️"):

        #保存会话信息
        save_session()

        #新建会话信息
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.current_session = save_current_time()
            save_session()

    #侧边栏标题
    st.subheader("伴侣信息")

    #昵称
    nick_name = st.text_input("昵称",placeholder="请输入伴侣的昵称",value=st.session_state.nick_name)
    if nick_name:
        st.session_state.nick_name = nick_name

    #性格
    character = st.text_area("性格",placeholder="请输入伴侣的性格",value=st.session_state.character)
    if character:
        st.session_state.character = character


# 遍历聊天信息
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("assistant").write(message["content"])


# 创建OPenai的客户端client
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com")

# 系统设定
System_prompt = """
    你叫%s，现在是用户的真实伴侣，请完全代入伴侣角色。
    规则：
        1. 每次只回1条消息
        2.禁止任何场景或状态描述性文字
        3.匹配用户的语言
        4.回复简短，像微信聊天一样
        5.有需要的话可以用❤️🌸等emoji表情
        6.用符合伴侣性格的方式对话
        7.回复的内容，要充分体现伴侣的性格特征
    伴侣性格：
        %s
    你必须严格遵守上述规则来回复用户。
"""

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
            {"role": "system", "content": System_prompt%( st.session_state.nick_name,st.session_state.character)},
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
    response_message = st.empty ()
    # 流式输出
    full_message = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_message += content
            response_message.chat_message("assistant").write(full_message)
    # 保存Ai的回复
    st.session_state.messages.append({"role": "assistant", "content": full_message})
    print("-------->",full_message)
